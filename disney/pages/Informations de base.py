import streamlit as st
import pandas as pd
from Analyse_de_base_hotels import répartition_des_notes,notes,notes1

liste = ['ParcDisney','Studio']
res = st.sidebar.multiselect('Sectionne',liste, ('ParcDisney','Studio'), key='monuments')
df = pd.DataFrame()
for i in res:
    if i == 'ParcDisney':
        df = df.append(pd.read_csv("C:/Users/laura/Downloads/Text-Mining-for-Disneyland-main (1)/Text-Mining-for-Disneyland-main/data_clean/Disneyland_Paris_clean.csv", sep=","))
    if i == 'Studio':
        df = df.append(pd.read_csv("C:/Users/laura/Downloads/Text-Mining-for-Disneyland-main (1)/Text-Mining-for-Disneyland-main/data_clean/Walt_Disney_Studios_Park_clean.csv", sep=","))


st.subheader('Donnée du lieux choisi')
st.write(df)

st.subheader('Répartition des notes attribué par le lieux choisie')
st.pyplot(répartition_des_notes(df))
st.subheader('Répartition des notes attribué par le lieux choisie')
st.pyplot(notes(df))
st.subheader('Répartition des notes attribué par le lieux choisie')
st.pyplot(notes1(df))

