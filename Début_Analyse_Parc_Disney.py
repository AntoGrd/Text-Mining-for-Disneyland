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
    # récupération du dataframe si l'on ne prend pas toutes les notes
    else:
        a = df.columns
        dfnew =  pd.DataFrame(columns=a)
        for i in note:
            print(i)
            dfnew = dfnew.append(df[df['Note']==i])
    X = parseur.fit_transform(dfnew['commentaire'])
    mdt = X.toarray()
    freq_mots = np.sum(mdt,axis=0)
    index = np.argsort(freq_mots)
    for i in range(freq_mots.shape[0]):
        index = index[::-1]
    #affichage des 5 mots qui ressortent le plus (ou un autre nombre si l'on a mit autre chose que 5)
    print("Nombre de mots distinct dans notre dataframe : "+ str(i))
    for j in range(nb_mots):
        print(np.asarray(parseur.get_feature_names())[index[j]],freq_mots[index[j]])
    print("")

# Exemple d'utilisation 
mots_significatif_par_note(parcDisney)
mots_significatif_par_note(parcDisney,[1,2,3],8)

