
import pandas as pd
import numpy as np
import ast
from gensim.models import Word2Vec
import matplotlib.pyplot as plt

parcDisney = pd.read_csv("/content/Disneyland_Paris_clean.csv", sep=",")
studio = pd.read_csv("/content/Walt_Disney_Studios_Park_clean.csv", sep = ',')

def most_similar_mots(df,liste_mots):
    liste = [ast.literal_eval(x) for x in df.commentaire]
    modele = Word2Vec(liste,vector_size=2,window=5)
    words = modele.wv
    for i in range (0,len(liste_mots)):
        print(liste_mots[i])
        print(words.most_similar(liste_mots[i]))
        print('\n')
        
mots = ['prix','attente','animation','enfant','très','long']
most_similar_mots(parcDisney, mots)

def most_similarity_mots(df,liste_mots):
    liste = [ast.literal_eval(x) for x in df.commentaire]
    modele = Word2Vec(liste,vector_size=2,window=5)
    words = modele.wv
    for i in range (0,len(liste_mots)):
        for j in range (0,len(liste_mots)):
            if i != j :
                print('Similarité entre', liste_mots[i], 'et',liste_mots[j])
                print(words.similarity(liste_mots[i], liste_mots[j]))
                print('\n')

most_similarity_mots(parcDisney, mots)

def representation_mots (df, liste_mots):
    liste = [ast.literal_eval(x) for x in df.commentaire]
    modele = Word2Vec(liste,vector_size=2,window=5)
    words = modele.wv
    df = pd.DataFrame(words.vectors,columns=["V1","V2"], index = words.key_to_index.keys())
    dfMots = df.loc[liste_mots,:]
    plt.scatter(dfMots.V1,dfMots.V2, s= 0.5)
    for i in range (dfMots.shape[0]):
        plt.annotate(dfMots.index[i],(dfMots.V1[i],dfMots.V2[i]))
    plt.show()
    
representation_mots(parcDisney, mots)

