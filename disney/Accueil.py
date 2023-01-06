import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from Analyse_de_base_hotels import nombre_avis_par_années

def main():
    st.header("home")
    st.title("titre")

liste = ['ParcDisney','Studio']
res = st.sidebar.multiselect('Sectionne',liste, ('ParcDisney','Studio'), key='monuments')
df = pd.DataFrame()
for i in res:
    if i == 'ParcDisney':
        df = df.append(pd.read_csv("C:/Users/laura/Downloads/Text-Mining-for-Disneyland-main (1)/Text-Mining-for-Disneyland-main/data_clean/Disneyland_Paris_clean.csv", sep=","))
    if i == 'Studio':
        df = df.append(pd.read_csv("C:/Users/laura/Downloads/Text-Mining-for-Disneyland-main (1)/Text-Mining-for-Disneyland-main/data_clean/Walt_Disney_Studios_Park_clean.csv", sep=","))


if __name__ == '__main__':
    main()

st.subheader('Donnée du lieux choisi')
st.write(df)







