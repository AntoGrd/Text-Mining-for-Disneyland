import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from Analyse_de_base_hotels import nombre_avis_par_années,répartition_des_notes
import mysql.connector
from cleanData import ProcessNouveauComm
import ast

#Nouveau commentaires 
st.write('Mise à jour des nouveaux commentaires')

date = ['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre']
selection_date  = st.selectbox(f'Choisissez la période des commentaires que vous voulez récupérer',date)

lieu = st.session_state['Hotels'].Lieux_disney.tolist()[1]

if lieu == "hotel_marvel" : 
            url = "https://www.tripadvisor.fr/Hotel_Review-g1182377-d262678-Reviews-Disney_Hotel_New_York_The_Art_of_Marvel-Chessy_Marne_la_Vallee_Seine_et_Marne_Ile_de_F.html"
elif lieu == "hotel_newport":
            url = "https://www.tripadvisor.fr/Hotel_Review-g1182377-d262679-Reviews-Disney_Newport_Bay_Club-Chessy_Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html"
elif lieu == "hotel_sequoia":
            url = "https://www.tripadvisor.fr/Hotel_Review-g5599092-d262682-Reviews-Disney_Sequoia_Lodge-Coupvray_Seine_et_Marne_Ile_de_France.html"
elif lieu == "hotel_cheyenne":
            url = "https://www.tripadvisor.fr/Hotel_Review-g226865-d262686-Reviews-Disney_Hotel_Cheyenne-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html"
elif lieu == "hotel_sante_fe":
            url = "https://www.tripadvisor.fr/Hotel_Review-g5599092-d262683-Reviews-Disney_Hotel_Santa_Fe-Coupvray_Seine_et_Marne_Ile_de_France.html"
elif lieu == "hotel_davy_crockett":
            url = "https://www.tripadvisor.fr/Hotel_Review-g1221082-d564634-Reviews-Disney_Davy_Crockett_Ranch-Bailly_Romainvilliers_Seine_et_Marne_Ile_de_France.html"
elif lieu == "Disneyland_Paris":
            url = "https://www.tripadvisor.fr/Attraction_Review-g226865-d189258-Reviews-Disneyland_Paris-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html"
elif lieu == "Walt_Disney_Studios_Park":
            url = "https://www.tripadvisor.fr/Attraction_Review-g226865-d285990-Reviews-Walt_Disney_Studios_Park-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html"


produit = st.session_state['Hotels']["Produit"].tolist()[0]
        

new_df = ProcessNouveauComm(url, selection_date, produit, st.session_state['Hotels'])

print(new_df.head())