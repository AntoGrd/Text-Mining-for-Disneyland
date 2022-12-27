#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A-Transformation en liste afin de réaliser la vectorisation
import ast
liste=[ast.literal_eval(x) for x in reviews.commentaire]

#importation de Word2Vec de Gensim pour la vectorisation
from gensim.models import Word2Vec
modele = Word2Vec(liste,vector_size=2,window=5)
words= modele.wv
df =pd.DataFrame(words.vectors, columns=['V1','V2'], index=words.key_to_index.keys())


#B- Sélection des principaux vecteurs

#(1) par sélection automatique des X premiers : 

dfMots= df[0:50]

#(2) par sélection manuelle des mots : 

    #a- export csv pour visualiser l'ensemble des mots
df.to_csv("words.vectors.txt",sep=";",header=True)

    #b - saisie  manuelle des termes à partir de la revue des hôtels sur booking et de la proximité spatiale des termes

mots = ['excellent','emplacement','personnel','dormir','impossible','boissons','restriction','personnel','inclus',
        'conciergerie','réception','accueil','weekend','famille','piscine','bouilloire','prix','cher','loin','équipement',
        'bébé','bon','bien','merveilleux','mauvaise','expérience','service',
        'baignoire','bouilloire','propre','propreté','manquait','poussière','cheveux','chambre','sommeil','buffet', 'déjeuner']

DfMots= df.loc[mots :]
DfMots.head(10)

#C- IMPORTANT : pour connaître la proximité entre 2 termes : regarder similarité cosinus 
#-- formule (produit scalaire des 2 vecteurs divisé par le produit des normes)

words.similarity("peluches","magique")

#-- méthode gensim : words.similarity( )


# -- pour regarder les mots les plus proches de la conjonction de 2 termes words.most_similar()

print(words.most_similar(positive=["magique"],negative =["décevant"],topn=3))


# -- pour regarder les mots les plus proches d'un terme donné.most_similar()
words.most_similar('buffet',topn=15)

