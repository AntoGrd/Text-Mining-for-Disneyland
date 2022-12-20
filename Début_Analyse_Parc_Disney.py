import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# Importation de la base de données
parcDisney = pd.read_csv("C:/Users/laura/Downloads/Text-Mining-for-Disneyland-main (1)/Text-Mining-for-Disneyland-main/data_clean/parc_disney_debut.csv", sep=",")
parcDisney.info( )

parcDisney.head() 
parcDisney['Date'].tail(1)
modalites = pd.unique(parcDisney['Note'])

print(parcDisney.Note.value_counts())

parseur = CountVectorizer()

def mot_significatif(df):
    X = parseur.fit_transform(df['commentaire'])
    mdt = X.toarray()
    freq_mots = np.sum(mdt,axis=0)
    index = np.argsort(freq_mots)
    for i in range(freq_mots.shape[0]):
        index = index[::-1]
    #affichage des 10 premiers
    print("FACTEUR : "+ str(i))
    for j in range(10):
        print(np.asarray(parseur.get_feature_names())[index[j]],freq_mots[index[j]])
    print("")
    
# Affichage des 10 mots qui ressortent le plus sur l'ensemble des commentaires
mot_significatif(parcDisney)

    
parseur_par_note = CountVectorizer()

def mots_significatif_par_note(df,note):
    # Récupération des commentaires asscocié à notre note
    dfnew = df[df['Note']==note]
    # Nombre de commentaire récupéré
    len(dfnew)
    X = parseur_par_note.fit_transform(dfnew['commentaire'])
    mdt = X.toarray()
    freq_mots = np.sum(mdt,axis=0)
    index = np.argsort(freq_mots)
    for i in range(freq_mots.shape[0]):
        index = index[::-1]
    #affichage des 10 premiers
    print("FACTEUR : "+ str(i))
    for j in range(10):
        print(np.asarray(parseur_par_note.get_feature_names())[index[j]],freq_mots[index[j]])
    print("")

# Affichage des mots qui ressortent le plus sur les commentaires de la note choisie 
mots_significatif_par_note(parcDisney,1)


