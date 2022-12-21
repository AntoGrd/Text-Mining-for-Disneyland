import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# Importation de la base de données
parcDisney = pd.read_csv("C:/Users/laura/Downloads/Text-Mining-for-Disneyland-main (1)/Text-Mining-for-Disneyland-main/data_clean/parc_disney_debut.csv", sep=",")
parcDisney.info( ) #200 avis

parcDisney.head() 
parcDisney['Date'].tail(1)
modalites = pd.unique(parcDisney['Note'])
print(parcDisney.Note.value_counts())

parseur = CountVectorizer()
# Fonction qui donne les 5 (par défault) mots les plus cités dans le dataframe (df) pour toutes les notes (par défault) 
def mots_significatif_par_note(df,note='tous',nb_mots = 5):
    # Récupération du dataframe pour toutes les notes)
    if (note == 'tous') :
        dfnew = df
    # Récupération du dataframe si l'on ne prend pas toutes les notes
    else:
        a = df.columns
        dfnew =  pd.DataFrame(columns=a)
        for i in note:
            print(i)
            dfnew = dfnew.append(df[df['Note']==i])
    X = parseur.fit_transform(dfnew['commentaire'])
    mdt = X.toarray()
    freq_mots = np.sum(mdt,axis=0)
    # Récupération des index des mots qui reviennent le plus (ordre décroissant)
    index = np.argsort(freq_mots)
    # On met les index dans l'ordre croissant
    index = np.flip(index)
    # Affichage des 5 mots qui ressortent le plus (ou un autre nombre si l'on a mit autre chose que 5)
    print("Nombre de mots distinct dans notre dataframe : "+ str(freq_mots.shape[0]))
    for k in range(nb_mots):
        print(np.asarray(parseur.get_feature_names())[index[k]],freq_mots[index[k]])
    print("")

# Exemple d'utilisation 
mots_significatif_par_note(df = parcDisney)
mots_significatif_par_note(df = parcDisney,note = [2,3,4], nb_mots = 8)
