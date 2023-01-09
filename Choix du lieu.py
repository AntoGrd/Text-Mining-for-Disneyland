import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit.components.v1 as components

# Declare the component:

def main():
    st.title("Avis-clients Trip Advisor")

if __name__ == '__main__':
    main()

liste = ['ParcDisney','Studio','Marvel','Newport Bay','Sequoia lodge','Cheyenne','Santa Fe','Davy Crockett']

res = st.selectbox(f'Faites votre sélection',liste)
# definition si un hôtel est sélectionné


# Create a text element and let the reader know the data is loading.

st.write(f'Résultat : {res}')
data_load_state = st.text('Loading data...')
data_load_state.text('Loading data...done!')

def load_data(nrows):
    data = pd.read_csv("hotel_sante_fe_clean.csv", sep=",") # Mettre à jour lors de la mise en place de la connexion avec la base
    return data
    
data = load_data(10000)

st.subheader('Aperçu des données du lieu choisi')
st.write(data)

# Contents of ~/my_app/main_page.py
import streamlit as st

st.markdown("# Choix du lieu 🎈")
st.sidebar.markdown("# Choix du lieu 🎈")
