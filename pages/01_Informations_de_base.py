import streamlit as st
import pandas as pd
from Analyse_de_base_hotels import nombre_avis_par_années,répartition_des_notes,notes,notes1


st.subheader('Donnée du lieux choisi')

st.subheader("Nombre d'avis par année")
st.bar_chart(nombre_avis_par_années(st.session_state['data']))
st.subheader('Répartition des notes attribué par le lieux choisie')
st.pyplot(répartition_des_notes(st.session_state['data']))
st.subheader('Répartition des notes attribué par le lieux choisie')
st.pyplot(notes(st.session_state['data']))
st.subheader('Répartition des notes attribué par le lieux choisie')
st.pyplot(notes1(st.session_state['data']))
