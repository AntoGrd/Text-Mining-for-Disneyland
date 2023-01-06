import streamlit as st
from Accueil import data

st.subheader('Répartition des notes attribué par le lieux choisie')
st.bar_chart(data.Note.value_counts())
