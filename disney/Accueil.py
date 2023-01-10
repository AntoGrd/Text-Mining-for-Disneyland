import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from Analyse_de_base_hotels import nombre_avis_par_années,répartition_des_notes

def main():
    st.header("home")
    st.title("titre")

if __name__ == '__main__':
    main()

liste = ['ParcDisney','Studio']
res = st.multiselect("Sectionne un (des) parc(s) et/ou un (des) hotel(s)) ",liste, (['ParcDisney']))
df = pd.DataFrame()
for i in res:
    if i == 'ParcDisney':
        df = df.append(pd.read_csv("C:/Users/laura/Downloads/Text-Mining-for-Disneyland-main (1)/Text-Mining-for-Disneyland-main/data_clean/Disneyland_Paris_clean.csv", sep=","))
    if i == 'Studio':
        df = df.append(pd.read_csv("C:/Users/laura/Downloads/Text-Mining-for-Disneyland-main (1)/Text-Mining-for-Disneyland-main/data_clean/Walt_Disney_Studios_Park_clean.csv", sep=","))

if 'data' not in st.session_state :
    valeur_def = df['Note'].unique()
else :
    valeur_def = st.session_state["data"].Note.unique()

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

st.sidebar.write('Date du commentaire')

if 'data' not in st.session_state :
    valeur_def = df['Annee_Avis'].unique()
else :
    valeur_def = st.session_state["data"].Annee_Avis.unique()

liste = df.Annee_Avis.unique()
res = st.multiselect('Sectionner la ou les années de séjour souhaité(s)',liste, valeur_def)
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

res = st.multiselect('Sectionner la ou les notes souhaité(s)',liste, (valeur_def))


if 'data' not in st.session_state :
    valeur_def = df['Mois_Avis'].unique()
else :
    valeur_def = st.session_state["data"].Mois_Avis.unique()

liste = df.Mois_Avis.unique()
res = st.multiselect('Sectionner la ou les mois de séjour souhaité(s)',liste, )
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

if 'data' not in st.session_state :
    valeur_def = df['Annee_Sejour'].unique()
else :
    valeur_def = st.session_state["data"].Annee_Sejour.unique()

liste = df.Annee_Sejour.unique()
res = st.multiselect('Sectionner la ou les années de séjour souhaité(s)',liste,)
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
        df.drop(df[df['Annee_Sejour'] == i].index,inplace=True)

if 'data' not in st.session_state :
    valeur_def = df['Mois_Sejour'].unique()
else :
    valeur_def = st.session_state["data"].Mois_Sejour.unique()

liste = df.Mois_Sejour.unique()
res = st.multiselect('Sectionner la ou les mois de séjour souhaité(s)',liste,)
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

st.subheader('Donnée du lieux choisi')
st.write(df)

if 'data' not in st.session_state : 
    st.session_state['data'] = df
st.text('Taille de la base sélectionner contient : ' + str(df.shape[0]) + " lignes")

st.write('La Base de données vous convient elle?')
button = st.button('Oui')
if button:
    st.session_state['data'] = df






