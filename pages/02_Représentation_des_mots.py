import streamlit as st
from Analyse_de_base_hotels import nuage_de_mots
from Récupération_des_x_mots_les_plus_présents import mots_significatif_par_note2,x_mots_plus_courants
from fonctions_analyse import representation_mots
from Idaviz import lda
from Similarité_de_mots import most_similar_mots,most_similarity_mots,representation_mots2
import numpy as np
from PIL import Image

st.title("Répartition des mots")


# Choix des différents graphiques
Diagramme = st.sidebar.radio(
    "Quel diagramme voulez-vous afficher ?",
    ("Histogramme des mots qui reviennent le plus", "Vecorisation de mots les plus courant",
    "Nuage de mots","graph antoine","Similarité des mots","Similarité des mots2", "Similarité des mots3"))

if Diagramme == "Histogramme des mots qui reviennent le plus":
    nb_mots = st.sidebar.slider('Combien voulez-vous afficher de mots? ', 0, 100, 5)
    st.sidebar.write('Nombre de mots choisi', nb_mots)
    st.sidebar.write('Le nombre de mots convient-il?')
    button = st.sidebar.button('Oui')
    st.session_state['nb_mots'] = nb_mots
    if button:
        st.header("Histogramme des mots qui reviennent le plus")
        if st.session_state['monument']  == 'Parcs':
            st.plotly_chart(mots_significatif_par_note2(st.session_state['Parcs'],st.session_state['nb_mots']))
        if st.session_state['monument']  == 'Hotels':
            st.plotly_chart(mots_significatif_par_note2(st.session_state['Hotels'],st.session_state['nb_mots']))

if Diagramme == "Vecorisation de mots les plus courant":
    nb_mots = st.sidebar.slider('Combien voulez-vous afficher de mots? ', 0, 100, 5)
    st.sidebar.write('Nombre de mots choisi', nb_mots)
    st.sidebar.write('Le nombre de mots convient-il?')
    button = st.sidebar.button('Oui')
    st.session_state['nb_mots'] = nb_mots
    if button:
        st.header("Vecorisation de mots les plus courant")
        if st.session_state['monument']  == 'Parcs':
            st.plotly_chart(representation_mots(st.session_state["Parcs"], "commentaire",st.session_state['nb_mots']))
        if st.session_state['monument']  == 'Hotels':
            st.plotly_chart(representation_mots(st.session_state["Hotels"], "commentaire",st.session_state['nb_mots']))              

if Diagramme == "Nuage de mots":
    image = np.array(Image.open("C:/Users/laura/dossier/mask.jpg"))
    st.header("Nuage de mots")
    if st.session_state['monument']  == 'Parcs':
        st.write(nuage_de_mots(st.session_state["Parcs"],image))
    if st.session_state['monument']  == 'Hotels':
        st.write(nuage_de_mots(st.session_state["Hotels"],image))             

if Diagramme == "graph antoine":
    if button:
        st.header("Graph antoine")
        if st.session_state['monument']  == 'Parcs':
            st.write(lda(st.session_state["Parcs"]))
        if st.session_state['monument']  == 'Hotels':
            st.write(lda(st.session_state["Hotels"]))

if Diagramme == 'Similarité des mots':
    nb_mots = st.sidebar.slider('Combien voulez-vous afficher de mots? ', 0, 100, 5)
    st.sidebar.write('Nombre de mots choisi', nb_mots)
    st.session_state['nb_mots'] = nb_mots
    if st.session_state['monument'] == 'Parcs':
        selection = x_mots_plus_courants(st.session_state['Parcs'],st.session_state['nb_mots'])
        option = st.selectbox('Selectionner un mots', selection)
        st.write(most_similar_mots(st.session_state['Parcs'], option))
    if st.session_state['monument'] == 'Hotels':
        selection = x_mots_plus_courants(st.session_state['Hotels'],st.session_state['nb_mots'])
        option = st.selectbox('Selectionner un mots', selection)
        st.write(most_similar_mots(st.session_state['Hotels'], option))


if Diagramme == 'Similarité des mots2':
    nb_mots = st.sidebar.slider('Combien voulez-vous afficher de mots? ', 0, 100, 5)
    st.sidebar.write('Nombre de mots choisi', nb_mots)
    st.session_state['nb_mots'] = nb_mots
    if st.session_state['monument'] == 'Parcs':
        selection = x_mots_plus_courants(st.session_state['Parcs'],st.session_state['nb_mots'])
        selection2 = x_mots_plus_courants(st.session_state['Parcs'],st.session_state['nb_mots'])
        option = st.selectbox('Selectionner un mots 1 ', selection)
        option2 = st.selectbox('Selectionner un mots 2 ', selection2)
        st.write(most_similarity_mots(st.session_state['Parcs'], option, option2))
    if st.session_state['monument'] == 'Hotels':
        selection = x_mots_plus_courants(st.session_state['Hotels'],st.session_state['nb_mots'])
        selection2 = x_mots_plus_courants(st.session_state['Hotels'],st.session_state['nb_mots'])
        option = st.selectbox('Selectionner un mots 1', selection)
        option2 = st.selectbox('Selectionner un mots 2', selection2)
        st.write(most_similarity_mots(st.session_state['Hotels'], option, option2))

if Diagramme == 'Similarité des mots3':
    nb_mots = st.sidebar.slider('Combien voulez-vous afficher de mots? ', 0, 100, 5)
    st.sidebar.write('Nombre de mots choisi', nb_mots)
    st.session_state['nb_mots'] = nb_mots
    if st.session_state['monument'] == 'Parcs':
        selection = x_mots_plus_courants(st.session_state['Parcs'],st.session_state['nb_mots'])
        option = st.multiselect('Selectionner un mots (Pour selectionner tous les mots plus rapidement cliquer sur controle et entrée)', selection, selection.head(10))
        st.pyplot(representation_mots2(st.session_state['Parcs'], option))
    if st.session_state['monument'] == 'Hotels':
        selection = x_mots_plus_courants(st.session_state['Hotels'],st.session_state['nb_mots'])
        option = st.multiselect('Selectionner un mots (Pour selectionner tous les mots plus rapidement cliquer sur controle et entrée)', selection, selection.head(10))
        st.pyplot(representation_mots2(st.session_state['Hotels'], option))
