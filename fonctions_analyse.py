# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 15:01:56 2023

@author: Sam
"""

import ast
from collections import Iterable
from nltk.probability import FreqDist
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.express as px
from gensim.models import keyedvectors
from sklearn import preprocessing
import numpy
from sklearn.decomposition import PCA
from plotly.offline import plot
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import os
from geopy.extra.rate_limiter import RateLimiter
import pycountry_convert as pc
from typing import Tuple
from tqdm import tqdm
tqdm.pandas()
from geopy.geocoders import Nominatim
from gensim.models import Word2Vec


#Transform list 
def flatten(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:        
             yield item

# Initialisation de SentimentIntensityAnalyzer.
#ajout des entiments 
def ScoreSentiment(vector):
    tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
     
    senti_list = []
    for i in vector:
        vs = tb(i).sentiment[0]
        if (vs > 0):
            senti_list.append('Positive')
        elif (vs < 0):
            senti_list.append('Negative')
        else:
            senti_list.append('Neutral') 
            
    return senti_list

#add columns sentiment for commentaire , titre_commentaire
#add columns without liste for commentaire , titre_commentaire
def add_Sentiment(df):
    
    liste = ["commentaire", "titre_commentaire"]
    
    for item in liste :
        
        liste_sentiment = ScoreSentiment(df[item])
        
        comm_ = [ast.literal_eval(x) for x in df[item].tolist()]

        comm_clean =[" ".join(doc) for doc in comm_]

        df["sentiment_" + str(item)] = liste_sentiment
        
        df[str(item)+ "_nolist"] = comm_clean
    
    return df 



#####################Graphique#########################
"""
allWords = ' '.join([twts for twts in d_sentiment["titre_commentaire_nolist"]])
wordCloud = WordCloud(width=500, height=300, random_state=5000, max_font_size=110).generate(allWords)

plt.imshow(wordCloud, interpolation="bilinear")
plt.axis('off')

plt.show()
"""

def wordCloud(df, colonne):
    
    allWords = ' '.join([twts for twts in df[str(colonne)]])
    wordCloud = WordCloud(width=500, height=300, random_state=5000, max_font_size=110).generate(allWords)

    plt.imshow(wordCloud, interpolation="bilinear")
    plt.axis('off')

    plt.show()
    
    

#select annee
def graph_sentiment(df , col, color, annee = "None"):
    
    if annee =="None":
        fig = px.histogram(df, x=col,color=color)
        
    else:
        d_annee = df[(df['Annee_Sejour'] == annee) ].reset_index(drop=True)
        fig = px.histogram(d_annee, x=col,color=color)
        
    fig.update_layout(
        title_text='Sentiment of reviews', # title of plot
        xaxis_title_text=color, # xaxis label
        yaxis_title_text='Count', # yaxis label
        bargap=0.2, 
        bargroupgap=0.1
    )
    
    
    return fig

def representation_mots(df,colonne,nb_mots = 10):
    

    liste = [ast.literal_eval(x) for x in df[str(colonne)]]
    modele = Word2Vec(liste,vector_size=2,window=5)
    words = modele.wv
    data = pd.DataFrame(words.vectors, columns=['V1','V2'], index=words.key_to_index.keys())
    mots2 = words.key_to_index.keys()
    mots2 = list(mots2)[0:nb_mots]
    dataMots2= data.loc[mots2]

    fig = px.scatter(dataMots2.V1,dataMots2.V2,text=dataMots2.index)

    fig.update_traces(textposition='top center')

    fig.update_layout(
        height=800,
    title_text='Représentation vectorielle des' + str(nb_mots) + "les plus présents"
    )
    
    fig.show()



###################Apprentissage non supervise#########################################"


os.chdir("C:/Users/Sam/Downloads/archive")

trained = keyedvectors.load_word2vec_format("GoogleNews-vectors-negative300.bin",binary=True,unicode_errors='ignore')

#commentaire = [ast.literal_eval(x) for x in d_sentiment["titre_commentaire"].tolist()]


#fonction pour transformer un document en vecteur
#à partir des tokens qui le composent
#entrée : doc à traiter
#         modèle préentrainé
#sortie : vecteur représentant le document

def my_doc_2_vec(doc, trained):
    #dimension de représentation
    p = trained.vectors.shape[1]
    #initialiser le vecteur
    vec = numpy.zeros(p)
    #nombre de tokens trouvés
    nb = 0
    #traitement de chaque token du document
    for tk in doc:
        #ne traiter que les tokens reconnus
        try:
            values = trained[tk]
            vec = vec + values
            nb = nb + 1.0
        except:
            pass
    #faire la moyenne des valeurs
    #uniquement si on a trové des tokens reconnus bien sûr
    if (nb > 0.0):
        vec = vec/nb
    #renvoyer le vecteur
    #si aucun token trouvé, on a un vecteur de valeurs nulles
    return vec

#creation matrice des mots
def CreateMatriceMot(df,colonne):

    #traiter les documents du corpus corpus
    docsVec = list()
    #pour chaque document du corpus nettoyé
    for doc in df[colonne]:
        #calcul de son vecteur
        vec = my_doc_2_vec(doc,trained)
        #ajouter dans la liste
        docsVec.append(vec)
        #transformer en matrice numpy
    matVec = numpy.array(docsVec)
    
    return matVec


def ACP(MatriceMot, nbcomp):
    
    Transposed_Dataset = pd.DataFrame(MatriceMot).T

    X_scaled = preprocessing.scale(Transposed_Dataset)


    X_std = preprocessing.StandardScaler().fit_transform(X_scaled)


    sklearn_pca = PCA(n_components = nbcomp) # Using PCA to remove cols which has less co-relation
    Y_sklearn = sklearn_pca.fit_transform(X_std) #fit_transform() is used to scale training data to learn parameters such as 

    return Y_sklearn

def elbow_method(Y_sklearn):
    """
    This is the function used to get optimal number of clusters in order to feed to the k-means clustering algorithm.
    """

    number_clusters = range(1, 7)  # Range of possible clusters that can be generated
    kmeans = [KMeans(n_clusters=i, max_iter = 600) for i in number_clusters] # Getting no. of clusters 

    score = [kmeans[i].fit(Y_sklearn).score(Y_sklearn) for i in range(len(kmeans))] # Getting score corresponding to each cluster.
    score = [i*-1 for i in score] # Getting list of positive scores.
    
    plt.plot(number_clusters, score)
    plt.xlabel('Number of Clusters')
    plt.ylabel('Score')
    plt.title('Elbow Method')
    plt.show()
    

def Kmeans(n_clusters, Y_sklearn) : 

    kmeans = KMeans(n_clusters= n_clusters, max_iter=400, algorithm = 'auto')# Partition 'n' no. of observations into 'k' no. of clusters. 
    fitted = kmeans.fit(Y_sklearn) # Fitting k-means model  to feature array
    prediction = kmeans.predict(Y_sklearn) # predicting clusters class '0' or '1' corresponding to 'n' no. of observations
    
    return fitted, prediction

def kmeans_clustering(Y_sklearn, fitted, prediction):
    """
    This function will predict clusters on training set and plot the visuals of clusters as well.
    """

    plt.scatter(Y_sklearn[:, 0], Y_sklearn[:, 1],c=prediction ,s=50, cmap='viridis') # Plotting scatter plot 
    centers2 = fitted.cluster_centers_ # It will give best possible coordinates of cluster center after fitting k-means
    plt.scatter(centers2[:, 0], centers2[:, 1],c='black', s=300, alpha=0.6);
    # As this can be seen from the figure, there is an outlier as well.
    




######Ajout des colonnes Pays_recod et Continent_recod####################

#permet d'obtenir le nom des continents
def get_continent_name(continent_code: str) -> str:
    continent_dict = {
        "NA": "North America",
        "SA": "South America",
        "AS": "Asia",
        "AF": "Africa",
        "OC": "Oceania",
        "EU": "Europe",
        "AQ" : "Antarctica"
    }
    return continent_dict[continent_code]


def get_continent(lat: float, lon:float) -> Tuple[str, str]:
    geolocator = Nominatim(user_agent="<username>@gmail.com", timeout=10)
    geocode = RateLimiter(geolocator.reverse, min_delay_seconds=1)

    location = geocode(f"{lat}, {lon}", language="fr")

    # for cases where the location is not found, coordinates are antarctica
    if location is None:
        return "Antarctica", "Antarctica"

    # extract country code
    address = location.raw["address"]
    country = address["country"]
    city = address["city"]
    lat = location.raw["lat"]
    lon = location.raw["lon"]
    
    #print(country)
    country_code = address["country_code"].upper()

    # get continent code from country code
    continent_code = pc.country_alpha2_to_continent_code(country_code)
    continent_name = get_continent_name(continent_code)
    
    return country, continent_name, lat, lon, city 

