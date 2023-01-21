import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from Analyse_de_base_hotels import nombre_avis_par_années,répartition_des_notes
import mysql.connector
from cleanData import clean_commentaire


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="disney_land"
)

mycursor = mydb.cursor()


def main():
    st.header("Trip Advisor Avis Clients")
   

if __name__ == '__main__':
    main()

# Choix du monument

monument = ['Choix du lieu',"Parcs", "Hotels"]
selection = st.selectbox(f'Choisissez si vous voulez des informations sur les parcs ou les hôtels',monument)
st.session_state['monument'] = selection

################################### PARCS ######################################################################

if selection == 'Parcs':
    st.write('Attention, vous devez valider vos données en cliquant sur Oui en bas de page')
    liste = ['ParcDisney 🌈','Studio 🎬']
    res = st.multiselect("Sélectionnez un (des) parc(s) et/ou un (des) hotel(s)) ",liste, liste)
    df = pd.DataFrame()
    for i in res:
        if i == 'ParcDisney 🌈':
            parc_disney = "SELECT titre_commentaire, commentaire, Mois_avis, Annee_avis, Mois_sejour, Annee_sejour, langue, Ville, Pays,Continent, Note, presence_photo, Situation FROM commentaire, date_avis, date_sejour,langues,lieu,lieux_disney, note, photo, produit, situations where commentaire.ID_note = note.ID_note and  commentaire.ID_photo = photo.ID_photo  and commentaire.ID_langue = langues.ID_langue and commentaire.ID_lieux_disney = lieux_disney.ID_lieux_disney and commentaire.ID_situation = situations.ID_situation and commentaire.ID_produit = produit.ID_produit and commentaire.ID_date_sejour = date_sejour.ID_date_sejour and commentaire.ID_date_avis = date_avis.ID_date_avis and commentaire.ID_lieu = lieu.ID_lieu and lieux_disney.Lieux_disney = 'Disneyland_Paris' "
            df = pd.read_sql(parc_disney,mydb)
            df = clean_commentaire(df)
        elif i == 'Studio 🎬':
            parc_studio = "SELECT titre_commentaire, commentaire, Mois_avis, Annee_avis, Mois_sejour, Annee_sejour, langue, Ville, Pays, Continent,Note, presence_photo, Situation FROM commentaire, date_avis, date_sejour,langues,lieu,lieux_disney, note, photo, produit, situations where commentaire.ID_note = note.ID_note and  commentaire.ID_photo = photo.ID_photo  and commentaire.ID_langue = langues.ID_langue and commentaire.ID_lieux_disney = lieux_disney.ID_lieux_disney and commentaire.ID_situation = situations.ID_situation and commentaire.ID_produit = produit.ID_produit and commentaire.ID_date_sejour = date_sejour.ID_date_sejour and commentaire.ID_date_avis = date_avis.ID_date_avis and commentaire.ID_lieu = lieu.ID_lieu and lieux_disney.Lieux_disney = 'Walt_Disney_Studios_Park' "
            df = pd.read_sql(parc_studio,mydb)
            df = clean_commentaire(df)
            
    if 'Parcs' not in st.session_state :
        valeur_def = df['Note'].unique()
    else :
        valeur_def = st.session_state["Parcs"].Note.unique()

    # Création de la liste de selection des notes
    liste = df.Note.unique()
    res = st.multiselect('Sectionnez la ou les notes souhaitée(s)',liste, valeur_def)
    sol = []
    # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    for i in liste:
        if i not in res :
            # On transfome les élément en entier (car c'est leur type dans le df)
            i = int(i)
            sol.append(i)
        # Ici si aucune valeur selectionnée, on a toute les données de la base
        if len(sol) != len(liste):
            # On supprime les éléments non choisis dans la liste déroulante à selection multiple
            for i in sol:
                df.drop(df[df['Note'] == i].index,inplace=True)

    st.write('Date du commentaire')

    if 'Parcs' not in st.session_state :
        valeur_def = df['Annee_avis'].unique()
    else :
        valeur_def = st.session_state["Parcs"].Annee_avis.unique()

    liste = df.Annee_avis.unique()
    res = st.multiselect("Sélectionnez la ou les années d'avis souhaité(es)",liste, liste)
    sol = []
    # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    for i in liste:
        if i not in res :
            sol.append(i)
        print(sol)
        # Ici si aucune valeur selectionnée, on a toutes les données en base
        if len(sol) != len(liste):
            # On supprime les éléments non choisis dans la liste déroulante à selection multiple
            for i in sol:
                df.drop(df[df['Annee_avis'] == i].index,inplace=True)

    if 'Parcs' not in st.session_state :
        valeur_def = df['Mois_avis'].unique()
    else :
        valeur_def = st.session_state["Parcs"].Mois_avis.unique()

    liste = df.Mois_avis.unique()
    res = st.multiselect("Sélectionnez la ou les mois d'avis souhaité(s)",liste, liste)
    sol = []
    # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    for i in liste:
        if i not in res :
            sol.append(i)
        # Ici si aucune valeur selectionnée, on a toutes les données en base
        if len(sol) != len(liste):
            # On supprime les éléments non choisis dans la liste déroulante à selection multiple
            for i in sol:
                df.drop(df[df['Mois_avis'] == i].index,inplace=True)

    st.write('Date du séjour')

    if 'Parcs' not in st.session_state :
        valeur_def = df.Annee_sejour.unique()
    else :
        valeur_def = st.session_state["Parcs"].Annee_sejour.unique()

    # liste = df.Annee_Sejour.unique()
    # res= st.multiselect('Sélectionnez la ou les années de séjour souhaité(s)',liste)
    # sol = []
    # # On crée une liste où se trouvent les notes qui ne sont pas dans la liste
    # for i in liste:
    #    if i not in res :
    #        sol.append(i)
    #    print(sol)
    #    # Ici si aucune valeur selectionnée, on a toutes les données en base
    #    if len(sol) != len(liste):
    #        # On supprime les éléments non choisis dans la liste déroulante à selection multiple
    #        for i in sol:
    #            df.drop(df[df['Annee_Sejour'] == i].index,inplace=True)

    if 'Parcs' not in st.session_state :
        valeur_def = df['Mois_sejour'].unique()
    else :
        valeur_def = st.session_state["Parcs"].Mois_sejour.unique()

    liste = df.Mois_sejour.unique()
    res = st.multiselect('Sélectionnez la ou les mois de séjour souhaité(s)',liste, liste)
    sol = []
    # On crée une liste où se trouvent les notes qui ne sont pas dans la liste
    for i in liste:
       if i not in res :
           sol.append(i)
       # Ici si aucune valeur selectionnée, on à toute les données en base
       if len(sol) != len(liste):
           # On supprime les éléments non choisis dans la liste déroulante à selection multiple
           for i in sol:
               df.drop(df[df['Mois_sejour'] == i].index,inplace=True)

    if 'Parcs' not in st.session_state :
        valeur_def = df['Situation'].unique()
    else :
        valeur_def = st.session_state["Parcs"].Situation.unique()

    liste = df.Situation.unique()
    res = st.multiselect('Sélectionnez la ou les situations souhaité(s)',liste, liste)
    sol = []
    # On crée une liste où se trouvent les notes qui ne sont pas dans la liste
    for i in liste:
       if i not in res :
           sol.append(i)
       # Ici si aucune valeur selectionnée, on a toutes les données en base
       if len(sol) != len(liste):
           # On supprime les éléments non choisie dans la liste déroulante a selection multiple
           for i in sol:
               df.drop(df[df['Situation'] == i].index,inplace=True) 
        
    if 'Parcs' not in st.session_state :
        valeur_def = df['Pays'].unique()
    else :
        valeur_def = st.session_state["Parcs"].Pays.unique()

    liste = df.Pays.unique()
    res = st.multiselect('Sectionner le ou les pays souhaité(s)',liste, liste)
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
    liste = ['Cheyenne 🤠','Davy_Crockett 🏹','Marvel🦸‍♀️','Newport 🏨','Santa_Fe 🏜️','Sequoia 🌲']
    res = st.multiselect("Sectionne un (des) parc(s) et/ou un (des) hotel(s)) ",liste, 'Cheyenne 🤠')
    df = pd.DataFrame()
    for i in res:
        if i == 'Cheyenne 🤠':
            hotel_cheyenne = "SELECT titre_commentaire, commentaire, Mois_avis, Annee_avis, Mois_sejour, Annee_sejour, langue, Ville, Pays, Continent,Note, presence_photo, Situation FROM commentaire, date_avis, date_sejour,langues,lieu,lieux_disney, note, photo, produit, situations where commentaire.ID_note = note.ID_note and  commentaire.ID_photo = photo.ID_photo  and commentaire.ID_langue = langues.ID_langue and commentaire.ID_lieux_disney = lieux_disney.ID_lieux_disney and commentaire.ID_situation = situations.ID_situation and commentaire.ID_produit = produit.ID_produit and commentaire.ID_date_sejour = date_sejour.ID_date_sejour and commentaire.ID_date_avis = date_avis.ID_date_avis and commentaire.ID_lieu = lieu.ID_lieu and lieux_disney.Lieux_disney = 'hotel_cheyenne' "
            df = pd.read_sql(hotel_cheyenne,mydb)
            df = clean_commentaire(df)
        elif i == 'Davy_Crockett 🏹':
            hotel_davy_crockett = "SELECT titre_commentaire, commentaire, Mois_avis, Annee_avis, Mois_sejour, Annee_sejour, langue, Ville, Pays, Continent,Note, presence_photo, Situation FROM commentaire, date_avis, date_sejour,langues,lieu,lieux_disney, note, photo, produit, situations where commentaire.ID_note = note.ID_note and  commentaire.ID_photo = photo.ID_photo  and commentaire.ID_langue = langues.ID_langue and commentaire.ID_lieux_disney = lieux_disney.ID_lieux_disney and commentaire.ID_situation = situations.ID_situation and commentaire.ID_produit = produit.ID_produit and commentaire.ID_date_sejour = date_sejour.ID_date_sejour and commentaire.ID_date_avis = date_avis.ID_date_avis and commentaire.ID_lieu = lieu.ID_lieu and lieux_disney.Lieux_disney = 'hotel_davy_crockett' "
            df = pd.read_sql(hotel_davy_crockett,mydb)
            df = clean_commentaire(df)
        elif i == 'Marvel 🦸‍♀️':
            hotel_marvel = "SELECT titre_commentaire, commentaire, Mois_avis, Annee_avis, Mois_sejour, Annee_sejour, langue, Ville, Pays, Continent,Note, presence_photo, Situation FROM commentaire, date_avis, date_sejour,langues,lieu,lieux_disney, note, photo, produit, situations where commentaire.ID_note = note.ID_note and  commentaire.ID_photo = photo.ID_photo  and commentaire.ID_langue = langues.ID_langue and commentaire.ID_lieux_disney = lieux_disney.ID_lieux_disney and commentaire.ID_situation = situations.ID_situation and commentaire.ID_produit = produit.ID_produit and commentaire.ID_date_sejour = date_sejour.ID_date_sejour and commentaire.ID_date_avis = date_avis.ID_date_avis and commentaire.ID_lieu = lieu.ID_lieu and lieux_disney.Lieux_disney = 'hotel_marvel' "
            df = pd.read_sql(hotel_marvel,mydb)
            df = clean_commentaire(df)
        elif i == 'Newport 🏨':
            hotel_newport = "SELECT titre_commentaire, commentaire, Mois_avis, Annee_avis, Mois_sejour, Annee_sejour, langue, Ville, Pays, Continent,Note, presence_photo, Situation FROM commentaire, date_avis, date_sejour,langues,lieu,lieux_disney, note, photo, produit, situations where commentaire.ID_note = note.ID_note and  commentaire.ID_photo = photo.ID_photo  and commentaire.ID_langue = langues.ID_langue and commentaire.ID_lieux_disney = lieux_disney.ID_lieux_disney and commentaire.ID_situation = situations.ID_situation and commentaire.ID_produit = produit.ID_produit and commentaire.ID_date_sejour = date_sejour.ID_date_sejour and commentaire.ID_date_avis = date_avis.ID_date_avis and commentaire.ID_lieu = lieu.ID_lieu and lieux_disney.Lieux_disney = 'hotel_newport' "
            df = pd.read_sql(hotel_newport,mydb)
            df = clean_commentaire(df)
        elif i == 'Santa_Fe 🏜️':
            hotel_sante_fe = "SELECT titre_commentaire, commentaire, Mois_avis, Annee_avis, Mois_sejour, Annee_sejour, langue, Ville, Pays, Continent,Note, presence_photo, Situation FROM commentaire, date_avis, date_sejour,langues,lieu,lieux_disney, note, photo, produit, situations where commentaire.ID_note = note.ID_note and  commentaire.ID_photo = photo.ID_photo  and commentaire.ID_langue = langues.ID_langue and commentaire.ID_lieux_disney = lieux_disney.ID_lieux_disney and commentaire.ID_situation = situations.ID_situation and commentaire.ID_produit = produit.ID_produit and commentaire.ID_date_sejour = date_sejour.ID_date_sejour and commentaire.ID_date_avis = date_avis.ID_date_avis and commentaire.ID_lieu = lieu.ID_lieu and lieux_disney.Lieux_disney = 'hotel_sante_fe' "
            df = pd.read_sql(hotel_sante_fe,mydb)
            df = clean_commentaire(df)
        elif i == 'Sequoia 🌲':
            hotel_sequoia = "SELECT titre_commentaire, commentaire, Mois_avis, Annee_avis, Mois_sejour, Annee_sejour, langue, Ville, Pays, Continent,Note, presence_photo, Situation FROM commentaire, date_avis, date_sejour,langues,lieu,lieux_disney, note, photo, produit, situations where commentaire.ID_note = note.ID_note and  commentaire.ID_photo = photo.ID_photo  and commentaire.ID_langue = langues.ID_langue and commentaire.ID_lieux_disney = lieux_disney.ID_lieux_disney and commentaire.ID_situation = situations.ID_situation and commentaire.ID_produit = produit.ID_produit and commentaire.ID_date_sejour = date_sejour.ID_date_sejour and commentaire.ID_date_avis = date_avis.ID_date_avis and commentaire.ID_lieu = lieu.ID_lieu and lieux_disney.Lieux_disney = 'hotel_sequoia' "
            df = pd.read_sql(hotel_sequoia,mydb)
            df = clean_commentaire(df)
        
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
        valeur_def_annee_avis_hotels = df['Annee_avis'].unique()
    else :
        valeur_def_annee_avis_hotels = st.session_state["Hotels"].Annee_avis.unique()

    liste_annee_avis_hotels = df.Annee_avis.unique()
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
        valeur_def = df['Mois_avis'].unique()
    else :
        valeur_def = st.session_state["Hotels"].Mois_avis.unique()

    liste = df.Mois_avis.unique()
    res = st.multiselect("Sectionner la ou les mois d'avis souhaité(s)",liste, liste)
    sol = []
    # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    for i in liste:
        if i not in res :
            sol.append(i)
        # Ici si aucune valeur selectionné, on à toute les données à la base
        if len(sol) != len(liste):
            # On supprime les éléments non choisie dans la liste déroulante a selection multiple
            for i in sol:
                df.drop(df[df['Mois_avis'] == i].index,inplace=True)

    st.write('Date du séjour')

    if 'Hotels' not in st.session_state :
        valeur_def = df.Annee_sejour.unique()
    else :
        valeur_def = st.session_state["Hotels"].Annee_sejour.unique()

    # liste = df.Annee_sejour.unique()
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
    #            df.drop(df[df['Annee_sejour'] == i].index,inplace=True)

    if 'Hotels' not in st.session_state :
        valeur_def = df['Mois_sejour'].unique()
    else :
        valeur_def = st.session_state["Hotels"].Mois_sejour.unique()

    liste = df.Mois_sejour.unique()
    res = st.multiselect('Sectionner la ou les mois de séjour souhaité(s)',liste, liste)
    sol = []
    # On crée une liste où se trouve les notes qui ne sont pas dans la liste
    for i in liste:
       if i not in res :
           sol.append(i)
       # Ici si aucune valeur selectionné, on à toute les données à la base
       if len(sol) != len(liste):
           # On supprime les éléments non choisie dans la liste déroulante a selection multiple
           for i in sol:
               df.drop(df[df['Mois_sejour'] == i].index,inplace=True)
 
    if 'Hotels' not in st.session_state :
        valeur_def = df['Pays'].unique()
    else :
        valeur_def = st.session_state["Hotels"].Pays.unique()

    liste = df.Pays.unique()
    res = st.multiselect('Sectionner la ou les pays souhaité(s)',liste, liste)
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

############################## Session_state ################################

    # Affichage du dataframe précédement selectionné
    st.subheader('Donnée du lieux choisi')
    st.write(df)

    st.text('Taille de la base sélectionner contient : ' + str(df.shape[0]) + " lignes")

    st.write('La Base de données vous convient elle?')
    # Si validation du bouton => création d'une variable globale (en gros qu'on peut utiliser dans toute l'appli)
    button = st.button('Oui')
    if button:
        st.session_state['Hotels'] = df