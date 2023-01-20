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
from sklearn.decomposition import LatentDirichletAllocation

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
import plotly.express as px

import sys

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
    
    fig = (px.line(df, x='Number of Clusters', y='Score',title="Méthode du coude", template='seaborn')).update_traces(mode='lines+markers')
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


#Plot topics function. Code from: https://scikit-learn.org/stable/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html
def plot_top_words(model, feature_names, n_top_words, title,nb_cluster):
    fig, axes = plt.subplots(nb_cluster, figsize=(30, 30), sharex=True)
    axes = axes.flatten()
    for topic_idx, topic in enumerate(model.components_):
        top_features_ind = topic.argsort()[:-n_top_words - 1:-1]
        top_features = [feature_names[i] for i in top_features_ind]
        weights = topic[top_features_ind]

        ax = axes[topic_idx]
        ax.barh(top_features, weights, height=0.7)
        ax.set_title(f'Topic {topic_idx +1}',
                     fontdict={'fontsize': 30})
        ax.invert_yaxis()
        ax.tick_params(axis='both', which='major', labelsize=20)
        for i in 'top right left'.split():
            ax.spines[i].set_visible(False)
        fig.suptitle(title, fontsize=40)
    plt.subplots_adjust(top=0.90, bottom=0.05, wspace=0.90, hspace=0.3)
    plt.show()

def text_cluistering(df, colonne, nb_cluster, ntherm) : 
    
    #inialisation dataframe
    Dcluster = pd.DataFrame()
    
    # initialize vectorizer
    vector = TfidfVectorizer(sublinear_tf=True, min_df=5, max_df=0.95)
    

    X = vector.fit_transform(df[str(colonne)])

    #creation cluster avce LDA
    lda = LatentDirichletAllocation(n_components=nb_cluster, learning_decay=0.9)
    X_lda = lda.fit(X)
    feature_names = vector.get_feature_names_out()

    top_word = plot_top_words(X_lda, feature_names, ntherm, ' ',  nb_cluster)

        
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
    
    
    #graphique methode coude
    coude = elbow_method(pca_vecs)
    
    
    #graphique Kmeans
    fig = px.scatter(Dcluster, x="1er axe", y="2ème axe", color="cluster",symbol="cluster", 
                     title="Clusters de mots avec les Kmeans") 

    fig.update_layout(
        title={
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})

    #return
    return coude,fig,top_word
