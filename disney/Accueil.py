import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from Analyse_de_base_hotels import nombre_avis_par_années

def main():
    st.header("home")
    st.title("titre")

if __name__ == '__main__':
    main()

liste = ['ParcDisney','Studio']

res = st.selectbox('Sectionne',liste)
st.write(f'resultat: {res}')

def load_data(nrows):
    data = pd.read_csv("C:/Users/lboutonnet/Desktop/Text-Mining-for-Disneyland-main/data_clean/Disneyland_Paris_clean.csv", sep=",")
    return data
    
data = load_data(10000)

st.subheader('Donnée du lieux choisi')
st.write(data)






