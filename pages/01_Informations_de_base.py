import streamlit as st
from Analyse_de_base_hotels import nombre_avis_par_années,répartition_des_notes,notes,notes1,photo_ou_non,situation_famille,par_pays

st.subheader('Donnée du lieux choisi')

#################### PARCS ##############
if st.session_state['monument']  == 'Parcs':
    # Choix des différents graphiques
    Diagramme = st.sidebar.radio(
        "Quel diagramme voulez-vous afficher ?",
        ("Nombre d'avis par année", "Répartition des notes", 'Différence des notes entre les français et les étrangers','Répartition des commentaires avec ou sans photos','Répartition des différents types de groupe',"Nombre d'avis par pays"))

    # Affichage des graphiques
    if Diagramme == "Nombre d'avis par année":
        st.subheader("Nombre d'avis par année")
        st.bar_chart(nombre_avis_par_années(st.session_state['Parcs']))
    if Diagramme == "Répartition des notes":
        st.subheader('Répartition des notes attribuées selon le lieu choisi')
        st.pyplot(répartition_des_notes(st.session_state['Parcs']))
    if Diagramme == "Différence des notes entre les Français et les étrangers":
        st.subheader('Différence des notes entre les Français et les étrangers')
        st.pyplot(notes1(st.session_state['Parcs']))
    if Diagramme == "Répartition des commentaires avec ou sans photos":
        st.subheader('Répartition des commentaires avec ou sans photos')
        st.pyplot(photo_ou_non(st.session_state['Parcs']))
    if Diagramme == "Répartition des différents types de groupe":
        st.subheader('Répartition des différents types de groupe')
        st.pyplot(situation_famille(st.session_state['Parcs']))
    if Diagramme == "Nombre d'avis par pays":
        st.subheader("Nombre d'avis par pays")
        st.bar_chart(par_pays(st.session_state['Parcs'])) 

####################### Hotels ###################
if st.session_state['monument']  == 'Hotels':
    # Choix des différents graphiques
    Diagramme = st.sidebar.radio(
        "Quel diagramme voulez-vous afficher ?",
        ("Nombre d'avis par année", "Répartition des notes", 'Différence des notes entre les français et les étrangers','Répartition des commentaires avec ou sans photos',"Nombre d'avis par pays"))

    # Affichage des graphiques
    if Diagramme == "Nombre d'avis par années*":
        st.subheader("Nombre d'avis par année")
        st.bar_chart(nombre_avis_par_années(st.session_state['Hotels']))
    if Diagramme == "Répartition des notes":
        st.subheader('Répartition des notes attribuées selon le lieu choisi')
        st.pyplot(répartition_des_notes(st.session_state['Hotels']))
    if Diagramme == "Différence des notes entre les Français et les étrangers":
        st.subheader('Différence des notes entre les Français et les étrangers')
        st.pyplot(notes1(st.session_state['Hotels']))
    if Diagramme == "Répartition des commentaires avec ou sans photos":
        st.subheader('Répartition des commentaires avec ou sans photos')
        st.pyplot(photo_ou_non(st.session_state['Hotels']))
    if Diagramme == "Nombre d'avis par pays":
        st.subheader("Nombre d'avis par pays")
        st.bar_chart(par_pays(st.session_state['Hotels'])) 
