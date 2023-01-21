import streamlit as st
from Text_clustering import text_cluistering


st.title('Analyse de texte')

nb_cluster = st.sidebar.slider('Combien de cluester souhaitez-vous? ', 0, 20, 3)
nb_mots = st.sidebar.slider('Combien de mots par cluster souhaitez-vous? ', 0 , 50, 10)

if st.session_state['monument'] == 'Parcs':
    retour = text_cluistering(st.session_state['Hotels_sentiment'],'titre_commentaire',nb_cluster,nb_mots)
    st.write(retour[0])
    st.write(retour[1])
    st.pyplot(retour[2])
if st.session_state['monument'] == 'Hotels':
    retour = text_cluistering(st.session_state['Hotels_sentiment'],'titre_commentaire',nb_cluster,nb_mots)
    st.write(retour[0])
    st.write(retour[1])
    st.pyplot(retour[2])
