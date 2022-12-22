import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# Importation de la base de données
parcDisney = pd.read_csv("C:/Users/laura/Downloads/Text-Mining-for-Disneyland-main (1)/Text-Mining-for-Disneyland-main/data_clean/parc_disney_debut.csv", sep=",")
parcDisney.info( ) #20685 avis

parcDisney.head()
#Récupération de l'année des premiers avis
parcDisney['Annee_Avis'][parcDisney['Annee_Avis'] != 'None'].tail(1)
modalites = pd.unique(parcDisney['Note'])
print(parcDisney.Note.value_counts())

parseur = CountVectorizer()

# Fonction qui donne les 5 (par défault) mots les plus cités dans le dataframe (df) pour toutes les notes (par défault) 
def mots_significatif_par_note(df, variable = 'toutes', modalité = 'toutes',  nb_mots = 5):
    # Récupération du dataframe pour toutes les notes)
    a = df.columns
    dfnew = pd.DataFrame(columns=a)
    # Si base complète on prend tout notre dataframe
    if (variable == 'toutes') :
        if (modalité == 'toutes'):
            dfnew = df
    # Si on choisie que quelques variables 
    else :
        # Si on prend toutes les modalités on prend tout notre dataFrame
        for i in range (0,len(variable)) : 
            if (modalité[i] == 'toutes'):
                dfnew = df
            else :
                # Sinon on récupère uniquement les lignes que l'on souhate
                for j in range (0,len(modalité[i])):
                    # On récupère l'ensemble des modalités de notre variable
                    dfnew = dfnew.append(df[df[variable[i]]==modalité[i][j]])
    parseur = CountVectorizer()
    X = parseur.fit_transform(dfnew['commentaire'])
    mdt = X.toarray()
    # On compte la fréquence de chaque mots dans notre DataFrame
    freq_mots = np.sum(mdt,axis=0)
    # Récupération des index des mots qui reviennent le plus (ordre décroissant)
    index = np.argsort(freq_mots)
    # On met les index dans l'ordre croissant
    index = np.flip(index)
    # On affiche les variables et les modalités de notre DataFrame et les nombre de mot total dans ce dernier
    print("Nombre de mots distinct dans notre dataframe contenant les variables : " + str(variable) ,"et les modalités " + str(modalité) ,": "+ str(freq_mots.shape[0]))
    # Affichage des 5 mots qui ressortent le plus (ou un autre nombre si l'on a mit autre chose que 5)
    for k in range(nb_mots):
        print(np.asarray(parseur.get_feature_names())[index[k]],freq_mots[index[k]])
    print("")

# Exemple d'utilisation 
mots_significatif_par_note(df = parcDisney)
mots_significatif_par_note(df = parcDisney, variable = ['Note','Pays'], modalité = [[4,5],[' France',' Espagne']], nb_mots = 8)

