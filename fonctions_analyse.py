# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 15:01:56 2023

@author: Sam
"""


import ast
#from collections import Iterable
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
import plotly.graph_objects as go
#from cleanData import clean_data_hotel,clean_commentaire,clean_data_parc

#Transform list 
#def flatten(lis):
#     for item in lis:
#         if isinstance(item, Iterable) and not isinstance(item, str):
#             for x in flatten(item):
#                 yield x
#         else:        
#             yield item

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
        
        liste_sentiment = ScoreSentiment(df[item].astype(str))
        
        comm_ = [ast.literal_eval(str(x)) for x in df[item].tolist()]

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
def graph_sentiment(df , col, annee = "None"):
    
    if annee == "None":
        data = df[col]
    else:
        data = df[(df['Annee_sejour'] == annee)][col]

    fig = go.Figure(data=[go.Histogram(x=data)])
    fig.update_layout(
        title='Sentiment of reviews',
        xaxis_title='Sentiment',
        yaxis_title='Count'
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
    title_text='Représentation vectorielle des ' + str(nb_mots) + " les plus présents"
    )
    return fig
    

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



def applyCountry(i):
    

        latitude = []
        longitude = []
        list_continent = []
        list_pays = []
        list_lat = []
        list_lon = []
        list_city = []
        
        geolocator  = Nominatim(user_agent = "geoapiExercises")

        
        os.chdir("C:/Users/Sam/Documents/GitHub/Text-Mining-for-Disneyland/data_translate")
        tab=pd.read_csv(str(i) + "_fr.csv")
        #if i == "Disneyland_Paris" or i == "Walt_Disney_Studios_Park" :
        #    tab = clean_data_parc(tab)
        #else:
        #    tab = clean_data_hotel(tab)
        
        #d_sentiment = add_Sentiment(tab) #ajouter la colonne sentiment sur les commentaires
        
        #ajouter la lattitude et longitudes des villes 
        for ville in tab['Ville'] : 
        
            try :
                location = geolocator.geocode(str(ville))
                latitude.append(location.latitude)
                longitude.append(location.longitude)
        
            except :
            
                latitude.append("None")
        
                longitude.append("None")
        
        tab['latitude_city'] = latitude
    
        tab['longitude_city'] = longitude
    
        latitude_city = tab['latitude_city'].tolist()
        longitude_city = tab['longitude_city'].tolist()
    
        for z in range(tab.shape[0]) : 
        
            try : 
                continent = get_continent(latitude_city[z], longitude_city[z])
        
                list_pays.append(continent[0])
                list_continent.append(continent[1]) 
                list_lat.append(continent[2])
                list_lon.append(continent[3])
                list_city.append(continent[4])
            except : 
                list_pays.append("None")
                list_continent.append("None")
                list_lat.append("None")
                list_lon.append("None")
                list_city.append("None")
            
            
        tab["Pays_recod"] = pd.Series(list_pays)
        tab["Contient_recod"] = pd.Series(list_continent)
        tab["lat_Pays"] = pd.Series(list_lat)
        tab["Lon_Pays"] = pd.Series(list_lon)
        tab["Ville_recod"] = pd.Series(list_city)
    
        
        latitude = []
        longitude = []
        list_continent = []
        list_pays = []
        list_lat = []
        list_lon = []
        list_city = []

        return tab


#localisation des touristes effectif
def getMap(df):
    
    D_map = df[["Pays_recod", "Contient_recod"]]


    D_map_bis = pd.DataFrame(D_map.groupby(by=(["Contient_recod"])).count())
    D_map_bis = D_map_bis.reset_index()
    D_map_bis.columns = ["continent", "effectif"]
    D_map_bis = D_map_bis[D_map_bis.continent != "None"]
    D_map_bis["effectif"] = D_map_bis.effectif.astype(float)
    
    lat_continent = [8.783195, 34.0479,54.526,54.526,-22.7359,-8.7832]
    long_continent = [34.508523, 100.6197,15.2551,-105.2551, 140.0187,-55.4915]
    continent = ["Africa", "Asia", "Europe", "North America", "Oceania", "South America"]

    df_map = pd.DataFrame(list(zip(continent, lat_continent, long_continent)),
                      columns =['continent','lat_continent','long_continent'])
     
    
    df_map = df_map.merge(D_map_bis, on='continent', how='left')

    
    fig = px.scatter_geo(df_map, lat ="lat_continent", lon= "long_continent" , color="continent",
                     hover_name="continent", size = df_map["effectif"],
                     projection="natural earth")
    fig.update_traces(textposition='top center')
    fig.update_layout(
       title_text = "Provenance des touristes" ,
        height=800)
    
    return fig
