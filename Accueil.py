import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from Analyse_de_base_hotels import nombre_avis_par_années,répartition_des_notes

def main():
    st.header("Choix du lieu")

if __name__ == '__main__':
    main()

# Choix du monument

monument = ['Choix du lieu','Parcs','Hotels']
selection = st.selectbox(f'Choisisez si vous voulez des informations sur les parcs ou les hotels',monument)
st.session_state['monument'] = selection

################################### PARCS ######################################################################

if selection == 'Parcs':
    st.write('Attention vous devez valider vos données en cliquant sur Oui en bas de page')
    liste = ['ParcDisney','Studio']
    res = st.multiselect("Sectionne un (des) parc(s) et/ou un (des) hotel(s)) ",liste, (['ParcDisney']))
    df = pd.DataFrame()
    for i in res:
        if i == 'ParcDisney':
            df = df.append(pd.read_csv("C:/Users/laura/OneDrive/Bureau/Disneyland_Paris_clean.csv", sep=","))
        if i == 'Studio':
            df = df.append(pd.read_csv("C:/Users/laura/OneDrive/Bureau/Walt_Disney_Studios_Park_clean.csv", sep=","))

    if 'Parcs' not in st.session_state :
        valeur_def = df['Note'].unique()
    else :
        valeur_def = st.session_state["Parcs"].Note.unique()

    # Création de la liste de selection des notes
    liste = df.Note.unique()
    res = st.multiselect('Sectionner la ou les notes souhaité(s)',liste, (valeur_def))
    sol = []
    # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    for i in liste:
        if i not in res :
            # On transfome les élément en entier (car c'est leur type dans le df)
            i = int(i)
            sol.append(i)
        # Ici si aucune valeur selectionner, on à toute les données à la base
        if len(sol) != len(liste):
            # On supprime les éléments non choisie dans la liste déroulante a selection multiple
            for i in sol:
                df.drop(df[df['Note'] == i].index,inplace=True)

    st.write('Date du commentaire')

    if 'Parcs' not in st.session_state :
        valeur_def = df['Annee_Avis'].unique()
    else :
        valeur_def = st.session_state["Parcs"].Annee_Avis.unique()

    liste = df.Annee_Avis.unique()
    res = st.multiselect("Sectionner la ou les années d'avis souhaité(s)",liste, valeur_def)
    sol = []
    # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    for i in liste:
        if i not in res :
            sol.append(i)
        print(sol)
        # Ici si aucune valeur selectionné, on à toute les données à la base
        if len(sol) != len(liste):
            # On supprime les éléments non choisie dans la liste déroulante a selection multiple
            for i in sol:
                df.drop(df[df['Annee_Avis'] == i].index,inplace=True)

    if 'Parcs' not in st.session_state :
        valeur_def = df['Mois_Avis'].unique()
    else :
        valeur_def = st.session_state["Parcs"].Mois_Avis.unique()

    liste = df.Mois_Avis.unique()
    res = st.multiselect("Sectionner la ou les mois d'avis souhaité(s)",liste, valeur_def)
    sol = []
    # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    for i in liste:
        if i not in res :
            sol.append(i)
        # Ici si aucune valeur selectionné, on à toute les données à la base
        if len(sol) != len(liste):
            # On supprime les éléments non choisie dans la liste déroulante a selection multiple
            for i in sol:
                df.drop(df[df['Mois_Avis'] == i].index,inplace=True)

    st.write('Date du séjour')

    if 'Parcs' not in st.session_state :
        valeur_def = df.Annee_Sejour.unique()
    else :
        valeur_def = st.session_state["Parcs"].Annee_Sejour.unique()

    # liste = df.Annee_Sejour.unique()
    # res= st.multiselect('Sectionner la ou les années de séjour souhaité(s)',liste)
    # sol = []
    # # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    # for i in liste:
    #    if i not in res :
    #        sol.append(i)
    #    print(sol)
    #    # Ici si aucune valeur selectionné, on à toute les données à la base
    #    if len(sol) != len(liste):
    #        # On supprime les éléments non choisie dans la liste déroulante a selection multiple
    #        for i in sol:
    #            df.drop(df[df['Annee_Sejour'] == i].index,inplace=True)

    if 'Parcs' not in st.session_state :
        valeur_def = df['Mois_Sejour'].unique()
    else :
        valeur_def = st.session_state["Parcs"].Mois_Sejour.unique()

    liste = df.Mois_Sejour.unique()
    res = st.multiselect('Sectionner la ou les mois de séjour souhaité(s)',liste, valeur_def)
    sol = []
    # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    for i in liste:
       if i not in res :
           sol.append(i)
       # Ici si aucune valeur selectionné, on à toute les données à la base
       if len(sol) != len(liste):
           # On supprime les éléments non choisie dans la liste déroulante a selection multiple
           for i in sol:
               df.drop(df[df['Mois_Sejour'] == i].index,inplace=True)

    if 'Parcs' not in st.session_state :
        valeur_def = df['Situation'].unique()
    else :
        valeur_def = st.session_state["Parcs"].Situation.unique()

    liste = df.Situation.unique()
    res = st.multiselect('Sectionner la ou les situations souhaité(s)',liste, valeur_def)
    sol = []
    # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    for i in liste:
       if i not in res :
           sol.append(i)
       # Ici si aucune valeur selectionné, on à toute les données à la base
       if len(sol) != len(liste):
           # On supprime les éléments non choisie dans la liste déroulante a selection multiple
           for i in sol:
               df.drop(df[df['Situation'] == i].index,inplace=True) 
    
    if 'Parcs' not in st.session_state :
        valeur_def = df['Pays'].unique()
    else :
        valeur_def = st.session_state["Parcs"].Pays.unique()

    liste = df.Pays.unique()
    res = st.multiselect('Sectionner la ou les pays souhaité(s)',liste, valeur_def)
    sol = []
    # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    for i in liste:
       if i not in res :
           sol.append(i)
       # Ici si aucune valeur selectionné, on à toute les données à la base
       if len(sol) != len(liste):
           # On supprime les éléments non choisie dans la liste déroulante a selection multiple
           for i in sol:
               df.drop(df[df['Pays'] == i].index,inplace=True) 

    # Affichage du dataframe précédement selectionné
    st.subheader('Donnée du lieux choisi')
    st.write(df)

    st.text('Taille de la base sélectionner contient : ' + str(df.shape[0]) + " lignes")

    st.write('La Base de données vous convient elle?')
    button = st.button('Oui')
    # Si validation du bouton => création d'une variable globale (en gros qu'on peut utiliser dans toute l'appli)
    if button:
        st.session_state['Parcs'] = df

###################### HOTELS ##############################################################################################################

if selection == 'Hotels':
    st.write('Attention vous devez valider vos données en cliquant sur Oui en bas de page')
    liste = ['Cheyenne']
    res = st.multiselect("Sectionne un (des) parc(s) et/ou un (des) hotel(s)) ",liste, (['Cheyenne']) )
    df = pd.DataFrame()
    for i in res:
        if i == 'Cheyenne':
            df = df.append(pd.read_csv("C:/Users/laura/OneDrive/Bureau/hotel_cheyenne_clean.csv", sep=","))

    if 'Hotels' not in st.session_state :
        valeur_def = df['Note'].unique()
    else :
        valeur_def = st.session_state["Hotels"].Note.unique()

    # Création de la liste de selection des notes
    liste = df.Note.unique()
    res = st.multiselect('Sectionner la ou les notes souhaité(s)',liste, (valeur_def))
    sol = []
    # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    for i in liste:
        if i not in res :
            # On transfome les élément en entier (car c'est leur type dans le df)
            i = int(i)
            sol.append(i)
        # Ici si aucune valeur selectionner, on à toute les données à la base
        if len(sol) != len(liste):
            # On supprime les éléments non choisie dans la liste déroulante a selection multiple
            for i in sol:
                df.drop(df[df['Note'] == i].index,inplace=True)

    st.write('Date du commentaire')

    if 'Hotels' not in st.session_state :
        valeur_def_annee_avis_hotels = df['Annee_Avis'].unique()
    else :
        valeur_def_annee_avis_hotels = st.session_state["Hotels"].Annee_Avis.unique()

    liste_annee_avis_hotels = df.Annee_Avis.unique()
    res_annee_avis_hotels = st.multiselect("Sectionner la ou les années d'avis souhaité(s)",liste_annee_avis_hotels, valeur_def_annee_avis_hotels)
    sol_annee_avis_hotels = []
    # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    for i in liste_annee_avis_hotels :
        if i not in res_annee_avis_hotels :
            sol_annee_avis_hotels.append(i)
        print(sol_annee_avis_hotels)
        # Ici si aucune valeur selectionné, on à toute les données à la base
        if len(sol_annee_avis_hotels) != len(liste_annee_avis_hotels):
            # On supprime les éléments non choisie dans la liste déroulante a selection multiple
            for i in sol_annee_avis_hotels:
                df.drop(df[df['Annee_Avis'] == i].index,inplace=True)

    if 'Hotels' not in st.session_state :
        valeur_def = df['Mois_Avis'].unique()
    else :
        valeur_def = st.session_state["Hotels"].Mois_Avis.unique()

    liste = df.Mois_Avis.unique()
    res = st.multiselect("Sectionner la ou les mois d'avis souhaité(s)",liste, valeur_def)
    sol = []
    # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    for i in liste:
        if i not in res :
            sol.append(i)
        # Ici si aucune valeur selectionné, on à toute les données à la base
        if len(sol) != len(liste):
            # On supprime les éléments non choisie dans la liste déroulante a selection multiple
            for i in sol:
                df.drop(df[df['Mois_Avis'] == i].index,inplace=True)

    st.write('Date du séjour')

    if 'Hotels' not in st.session_state :
        valeur_def = df.Annee_Sejour.unique()
    else :
        valeur_def = st.session_state["Hotels"].Annee_Sejour.unique()

    # liste = df.Annee_Sejour.unique()
    # res= st.multiselect('Sectionner la ou les années de séjour souhaité(s)',liste,)
    # sol = []
    # # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    # for i in liste:
    #    if i not in res :
    #        sol.append(i)
    #    print(sol)
    #    # Ici si aucune valeur selectionné, on à toute les données à la base
    #    if len(sol) != len(liste):
    #        # On supprime les éléments non choisie dans la liste déroulante a selection multiple
    #        for i in sol:
    #            df.drop(df[df['Annee_Sejour'] == i].index,inplace=True)

    if 'Hotels' not in st.session_state :
        valeur_def = df['Mois_Sejour'].unique()
    else :
        valeur_def = st.session_state["Hotels"].Mois_Sejour.unique()

    liste = df.Mois_Sejour.unique()
    res = st.multiselect('Sectionner la ou les mois de séjour souhaité(s)',liste, valeur_def)
    sol = []
    # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    for i in liste:
       if i not in res :
           sol.append(i)
       # Ici si aucune valeur selectionné, on à toute les données à la base
       if len(sol) != len(liste):
           # On supprime les éléments non choisie dans la liste déroulante a selection multiple
           for i in sol:
               df.drop(df[df['Mois_Sejour'] == i].index,inplace=True)
 
    if 'Hotels' not in st.session_state :
        valeur_def = df['Pays'].unique()
    else :
        valeur_def = st.session_state["Hotels"].Pays.unique()

    liste = df.Pays.unique()
    res = st.multiselect('Sectionner la ou les pays souhaité(s)',liste, valeur_def)
    sol = []
    # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    for i in liste:
       if i not in res :
           sol.append(i)
       # Ici si aucune valeur selectionné, on à toute les données à la base
       if len(sol) != len(liste):
           # On supprime les éléments non choisie dans la liste déroulante a selection multiple
           for i in sol:
               df.drop(df[df['Pays'] == i].index,inplace=True) 

    # Affichage du dataframe précédement selectionné
    st.subheader('Donnée du lieux choisi')
    st.write(df)

    st.text('Taille de la base sélectionner contient : ' + str(df.shape[0]) + " lignes")

    st.write('La Base de données vous convient elle?')
    # Si validation du bouton => création d'une variable globale (en gros qu'on peut utiliser dans toute l'appli)
    button = st.button('Oui')
    if button:
        st.session_state['Hotels'] = df
