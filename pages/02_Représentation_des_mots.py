import streamlit as st
from Récupération des x mots les plus présents.py import mots_significatif_par_note2
from fonctions_analyse import representation_mots

st.title("Répartition des mots")

nb_mots = st.slider('Combien voulez-vous afficher de mots? ', 0, 100, 5)
st.write('Nombre de mots choisi', nb_mots)

st.write('Le nombre de mots convient-il?')
button = st.button('Oui')
if button:
    st.session_state['nb_mots'] = nb_mots
    if st.session_state['monument']  == 'Parcs':
        st.pyplot(mots_significatif_par_note2(st.session_state['Parcs'],st.session_state['nb_mots']))
    if st.session_state['monument']  == 'Hotels':
        st.pyplot(mots_significatif_par_note2(st.session_state['Hotels'],st.session_state['nb_mots']))

st.pyplot(representation_mots(st.session_state["Parcs"], "commentaire"))
