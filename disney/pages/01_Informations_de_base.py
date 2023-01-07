import streamlit as st
import pandas as pd
from Analyse_de_base_hotels import répartition_des_notes,notes,notes1

liste = ['ParcDisney','Studio']
res = st.sidebar.multiselect("Sectionne un (des) parc(s) et/ou un (des) hotel(s)) ",liste, ('ParcDisney','Studio'))
df = pd.DataFrame()
for i in res:
    if i == 'ParcDisney':
        df = df.append(pd.read_csv("C:/Users/laura/Downloads/Text-Mining-for-Disneyland-main (1)/Text-Mining-for-Disneyland-main/data_clean/Disneyland_Paris_clean.csv", sep=","))
    if i == 'Studio':
        df = df.append(pd.read_csv("C:/Users/laura/Downloads/Text-Mining-for-Disneyland-main (1)/Text-Mining-for-Disneyland-main/data_clean/Walt_Disney_Studios_Park_clean.csv", sep=","))

liste = ['1','2','3','4','5']
res = st.sidebar.multiselect('Sectionner la ou les notes souhaité',liste, ('1','2','3','4','5'))
sol = []
for i in liste:
  if i not in res :
    i = int(i)
    sol.append(i)
for i in sol:
    df.drop(df[df['Note'] == i].index,inplace=True)
print(df['Note'])

st.subheader('Donnée du lieux choisi')
st.write(df)

st.subheader('Répartition des notes attribué par le lieux choisie')
st.pyplot(répartition_des_notes(df))
st.subheader('Répartition des notes attribué par le lieux choisie')
st.pyplot(notes(df))
st.subheader('Répartition des notes attribué par le lieux choisie')
st.pyplot(notes1(df))
