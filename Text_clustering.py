# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 15:48:46 2023

@author: Sam
"""

# import required sklearn libs
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# import other required libs
import pandas as pd
import numpy as np

# viz libs
import matplotlib.pyplot as plt
import seaborn as sns

import os 
from gensim.models import keyedvectors
import ast
from plotly.offline import plot

import sys

sys.setrecursionlimit(20000)
os.chdir("C:/Users/sibghi/Documents/GitHub/Text-Mining-for-Disneyland/data_clean")

d_sentiment = pd.read_csv("hotel_marvel_clean.csv", sep=",")

os.chdir("C:/Users/Sam/Downloads/archive")

trained = keyedvectors.load_word2vec_format("GoogleNews-vectors-negative300.bin",binary=True,unicode_errors='ignore')


#fonction pour transformer un document en vecteur
#à partir des tokens qui le composent
#entrée : doc à traiter
#         modèle préentrainé
#sortie : vecteur représentant le document
def my_doc_2_vec(doc,trained):
    #dimension de représentation
    p = trained.vectors.shape[1]
    #initialiser le vecteur
    vec = np.zeros(p)
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


#fonction pour représenter un corpus à partir d'une représentation
#soit entraînée, soit pré-entraînée
#sortie : représentation matricielle
def my_corpora_2_vec(corpora,trained):
    docsVec = list()
    #pour chaque document du corpus nettoyé
    for doc in corpora:
        #calcul de son vecteur
        vec = my_doc_2_vec(doc,trained)
        #ajouter dans la liste
        docsVec.append(vec)
    #transformer en matrice numpy
    matVec = np.array(docsVec)
    return matVec

def elbow_method(Y_sklearn):
    """
    This is the function used to get optimal number of clusters in order to feed to the k-means clustering algorithm.
    """

    number_clusters = range(1, 7)  # Range of possible clusters that can be generated
    kmeans = [KMeans(n_clusters=i, max_iter = 600) for i in number_clusters] # Getting no. of clusters 

    score = [kmeans[i].fit(Y_sklearn).score(Y_sklearn) for i in range(len(kmeans))] # Getting score corresponding to each cluster.
    score = [i*-1 for i in score] # Getting list of positive scores.
    
    df = pd.DataFrame()
    df["Number of Clusters"] = number_clusters
    df["Score"] = score
    
    fig = px.scatter(df, x="Number of Clusters", y="Score", 
                 title="Méthode du coude") 

    fig.update_layout(
        title={
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})

    return fig
    
  
def get_top_keywords(n_terms, X,clusters,vectorizer):
    """This function returns the keywords for each centroid of the KMeans"""

    df = pd.DataFrame(X.todense()).groupby(clusters).mean() # groups tf idf vector per cluster
    terms = vectorizer.get_feature_names_out() # access to tf idf terms
    dicts = {}
    for i,r in df.iterrows():
        dicts['Cluster {}'.format(i)] = ','.join([terms[t] for t in np.argsort(r)[-n_terms:]]) 
        
    return dicts



def text_cluistering(df, colonne, nb_cluster) : 
    
    #inialisation dataframe
    Dcluster = pd.DataFrame()
    
    # initialize vectorizer
    vector = TfidfVectorizer(sublinear_tf=True, min_df=5, max_df=0.95)
    

    X = vector.fit_transform(df[str(colonne)])

        
    # initialize KMeans with 3 clusters
    kmeans = KMeans(n_clusters=nb_cluster, max_iter=400, random_state=42)
    kmeans.fit(X)
    #kmeans.fit(X)
    clusters = kmeans.labels_
    
    Sim = get_top_keywords(10,X,clusters,vector) #cluster des mots

    # initialize PCA with 2 components
    pca = PCA(n_components=2, random_state=42)
    # pass X to the pca
        

    pca_vecs = pca.fit_transform(X.toarray())
    
    # save the two dimensions in x0 and x1
    x0 = pca_vecs[:, 0]
    x1 = pca_vecs[:, 1]

    # assign clusters and PCA vectors to columns in the original dataframe
    Dcluster['cluster'] = clusters
    Dcluster['1er axe'] = x0
    Dcluster['2ème axe'] = x1


    dicts = {}
    for i in range(nb_cluster):
        
        dicts[i] = "Cluster_" + str(i)
        
        
    Dcluster['cluster'] = Dcluster['cluster'].map(dicts)
    Dcluster = pd.DataFrame(Dcluster)
    
    coude = elbow_method(pca_vecs)

    
    return Dcluster, Sim, coude


a, b , c = text_cluistering(d_sentiment, "titre_commentaire", 2)


import plotly.express as px


fig = px.scatter(a, x="1er axe", y="2ème axe", color="cluster",symbol="cluster", 
                 title="Clusters de mots avec les Kmeans") 

fig.update_layout(
    title={
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

plot(fig)


plot()



#CAH à partir de scipy
from scipy.cluster.hierarchy import dendrogram, linkage,fcluster

#pour transformation en MDT
from sklearn.feature_extraction.text import CountVectorizer


#fonction pour construire une typologie à partir
#d'une représentation des termes, qu'elle soit entraînée ou pré-entraînée
#seuil par défaut = 1, mais le but est d'avoir 4 groupes
#corpus ici se présente sous la forme d'une liste de listes de tokens
def my_cah_from_doc2vec(df, colonne,trained,seuil=1.0,nbTermes=7, nbcluster = 5):

    #matrice doc2vec pour la représentation à 100 dim.
    #entraînée via word2vec sur les documents du corpus
    mat = my_corpora_2_vec(df[str(colonne)],trained)

    #dimension
    #mat.shape

    #générer la matrice des liens
    Z = linkage(mat,method='ward',metric='euclidean')

    #affichage du dendrogramme avec le seuil
    plt.title("CAH")
    dendrogram(Z,orientation='left',color_threshold=seuil)
    plt.show()

    #découpage en 4 classes
    grCAH = fcluster(Z,t=seuil,criterion='distance')
    #print(grCAH)

    #***************************
    #interprétation des clusters
    #***************************
    
    #parseur
    parseur = CountVectorizer(binary=True)

    
    #matrice MDT
    mdt = parseur.fit_transform(df[str(colonne)]).toarray()
    print("Dim. matrice documents-termes = {}".format(mdt.shape))
    
    #passer en revue les groupes
    for num_cluster in range(np.max(grCAH)):
        print("")
        #numéro du cluster à traiter
        print("Numero du cluster = {}".format(num_cluster+1))
        groupe = np.where(grCAH==num_cluster+1,1,0)
        effectifs = np.unique(groupe,return_counts=True)
        print("Effectifs = {}".format(effectifs[1][1]))
        #calcul de co-occurence
        cooc = np.apply_along_axis(func1d=lambda x: np.sum(x*groupe),axis=0,arr=mdt)
        #print(cooc)
        #création d'un data frame intermédiaire
        tmpDF = pd.DataFrame(data=cooc,columns=['freq'],index=parseur.get_feature_names_out())    
        #affichage des "nbTermes" termes les plus fréquents
        print(tmpDF.sort_values(by='freq',ascending=False).iloc[:nbTermes,:])
        
    #renvoyer l'indicateur d'appartenance aux groupes
    return grCAH, mat


my_cah_from_doc2vec(d_sentiment, "titre_commentaire",trained,seuil=1.0,nbTermes=7)
