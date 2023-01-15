import streamlit as st
from X_mots import mots_significatif_par_notes2

nb_mots = st.slider('Combien voulez-vous afficher de mots? ', 0, 20, 5)
st.write('Nomnre de mots choisi', nb_mots)

st.write('Le nombre de mots convient-il ?')
button = st.button('Oui')
if button : 
  st.session_state['nb_mots'] = nb_mots
  
st.title("Répartition des mots")
st.pyplot(mots_sigificatif_par_note2(st.session_state['data'],st.session_state['nb_mots']))
