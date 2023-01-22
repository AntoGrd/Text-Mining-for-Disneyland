import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from Analyse_de_base_hotels import nombre_avis_par_années,répartition_des_notes
import mysql.connector
from cleanData import ProcessNouveauComm
import ast
import datetime


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="disney_land"
)

mycursor = mydb.cursor()

#Nouveau commentaires 
st.title('Mise à jour des nouveaux commentaires')

date = ['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre']
selection_date  = st.selectbox(f'Choisissez la période des commentaires que vous voulez récupérer',date)


if st.session_state['monument'] == 'Parcs':
    
    lieu = st.session_state['Parc'].Lieux_disney.tolist()[1]
    
    if lieu == "Disneyland_Paris":
            url = "https://www.tripadvisor.fr/Attraction_Review-g226865-d189258-Reviews-Disneyland_Paris-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html"
    elif lieu == "Walt_Disney_Studios_Park":
            url = "https://www.tripadvisor.fr/Attraction_Review-g226865-d285990-Reviews-Walt_Disney_Studios_Park-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html"
    
    produit = st.session_state['Parc']["Produit"].tolist()[0]

    st.write('Veuillez mettre à jour la base de donnée en cliquant sur le bouton ci-dessous : ')

    if st.button('Mise à jour') :
    
        new_df = ProcessNouveauComm(url, selection_date, produit, st.session_state['Parc'])        
        
        
        current_year = datetime.datetime.now().year

        #insertion lignes lieu 
        mycursor.execute("SELECT DISTINCT Ville FROM lieu")
        Ville = [table[0] for table in mycursor.fetchall()]
        
        for i in range(len(new_df)) :
            
            ville = new_df.Ville_recod[i]
            pays = new_df.Pays_recod[i]
            Continent = new_df.Contient_recod[i]
            
            if ville not in Ville:
                
              sql = "INSERT INTO lieu VALUES(%s, %s, %s, %s)"
              mycursor.execute(sql, ("SELECT MAX(ID_lieu) + 1 FROM lieu",ville, pays, Continent))

        #insertion date_avis
        #query to check if the month and year exist
        query = "SELECT * FROM date_avis WHERE Mois_avis = '{}' AND Annee_avis = {}".format(selection_date, current_year)
        # execute the query
        mycursor.execute(query)
        # store the result in a variable
        result = mycursor.fetchall()
        # check if the result is empty or not
        if len(result) == 0:
             
            sql = "INSERT INTO date_avis VALUES(%s, %s, %s)"
            mycursor.execute(sql, ("SELECT MAX(ID_date_avis) + 1 FROM date_avis",selection_date,current_year))
        
        #insertion date_sejour
        #query to check if the month and year exist
        query = "SELECT * FROM date_sejour WHERE Mois_sejour = '{}' AND Annee_sejour = {}".format(selection_date, current_year)
        # execute the query
        mycursor.execute(query)
        # store the result in a variable
        result = mycursor.fetchall()
        # check if the result is empty or not
        if len(result) == 0:
             
            sql = "INSERT INTO date_sejour VALUES(%s, %s, %s)"
            mycursor.execute(sql, ("SELECT MAX(ID_date_sejour) + 1 FROM date_sejour",selection_date,current_year))
            
        
        #insertion langue 
        mycursor.execute("SELECT DISTINCT langue FROM langues")
        Langue = [table[0] for table in mycursor.fetchall()]
        
        for i in range(len(new_df)) :
            
            langue = new_df.langue[i]
            
            if langue not in Langue:
                
              sql = "INSERT INTO lieu VALUES(%s, %s)"
              mycursor.execute(sql, ("SELECT MAX(ID_langue) + 1 FROM langues",langue))
        
       
        st.write('La mise à jour à bien été réalisé')
        
        
    
if st.session_state['monument'] == 'Hotels':
    
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
    
    produit = st.session_state['Hotels']["Produit"].tolist()[0]
    
    st.write('Veuillez mettre à jour la base de donnée en cliquant sur le bouton ci-dessous : ')
    
    if st.button('Mise à jour') :
    
        new_df = ProcessNouveauComm(url, selection_date, produit, st.session_state['Hotels'])
        
        current_year = datetime.datetime.now().year

        
        #insertion lignes lieu 
        mycursor.execute("SELECT DISTINCT Ville FROM lieu")
        Ville = [table[0] for table in mycursor.fetchall()]
        
        for i in range(len(new_df)) :
            
            ville = new_df.Ville_recod[i]
            pays = new_df.Pays_recod[i]
            Continent = new_df.Contient_recod[i]
            
            if ville not in Ville:
                
              sql = "INSERT INTO lieu VALUES(%s, %s, %s, %s)"
              mycursor.execute(sql, ("SELECT MAX(ID_lieu) + 1 FROM lieu",ville, pays, Continent))

        #insertion date_avis
        #query to check if the month and year exist
        query = "SELECT * FROM date_avis WHERE Mois_avis = '{}' AND Annee_avis = {}".format(selection_date, current_year)
        # execute the query
        mycursor.execute(query)
        # store the result in a variable
        result = mycursor.fetchall()
        # check if the result is empty or not
        if len(result) == 0:
             
            sql = "INSERT INTO date_avis VALUES(%s, %s, %s)"
            mycursor.execute(sql, ("SELECT MAX(ID_date_avis) + 1 FROM date_avis",selection_date,current_year))
        
        #insertion date_sejour
        #query to check if the month and year exist
        query = "SELECT * FROM date_sejour WHERE Mois_sejour = '{}' AND Annee_sejour = {}".format(selection_date, current_year)
        # execute the query
        mycursor.execute(query)
        # store the result in a variable
        result = mycursor.fetchall()
        # check if the result is empty or not
        if len(result) == 0:
             
            sql = "INSERT INTO date_sejour VALUES(%s, %s, %s)"
            mycursor.execute(sql, ("SELECT MAX(ID_date_sejour) + 1 FROM date_sejour",selection_date,current_year))
            
        
        #insertion langue 
        mycursor.execute("SELECT DISTINCT langue FROM langues")
        Langue = [table[0] for table in mycursor.fetchall()]
        
        for i in range(len(new_df)) :
            
            langue = new_df.langue[i]
            
            if langue not in Langue:
                
              sql = "INSERT INTO lieu VALUES(%s, %s)"
              mycursor.execute(sql, ("SELECT MAX(ID_langue) + 1 FROM langues",langue))
        
       
        st.write('La mise à jour à bien été réalisé')


