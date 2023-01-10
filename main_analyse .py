# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 17:25:42 2023

@author: Sam
"""

from fonctions_analyse import get_continent, add_Sentiment
import pandas as pd
import os
from geopy.geocoders import Nominatim
from tqdm import tqdm
tqdm.pandas()
from joblib import Parallel, delayed
import joblib
from cleanData import clean_data_hotel, clean_data_parc,clean_commentaire


geolocator  = Nominatim(user_agent = "geoapiExercises")

nom_sites =  ["hotel_marvel","hotel_newport","hotel_sequoia","hotel_cheyenne", "hotel_sante_fe","hotel_davy_crockett"]
        
import dask
from dask import delayed      

for i in nom_sites:
    
    y = delayed(applyCountry)(str(i))
    tab = pd.DataFrame(y.compute())
    
    tab.to_csv("C:/Users/Sam/Documents/GitHub/Text-Mining-for-Disneyland/data_translate/" + str(i) + "_ope.csv")
    
    
        
def applyCountry(i):
    

        latitude = []
        longitude = []
        list_continent = []
        list_pays = []
        list_lat = []
        list_lon = []
        list_city = []
        

        
        os.chdir("C:/Users/Sam/Documents/GitHub/Text-Mining-for-Disneyland/data_translate")
        tab=pd.read_csv(str(i) + "_fr.csv")
        tab = clean_data_hotel(tab)
        tab = clean_commentaire(tab)
        
        #d_sentiment = add_Sentiment(tab) #ajouter la colonne sentiment sur les commentaires
        
        #ajouter la lattitude et longitudes des villes 
        for ville in tab['Ville'] : 
        
            try :
                location = geolocator.geocode(str(ville))
                latitude.append(location.latitude)
                longitude.append(location.longitude)
        
            except :
            
                latitude.append("None")
        
                longitude.append("None")
        
        tab['latitude_city'] = latitude
    
        tab['longitude_city'] = longitude
    
        latitude_city = tab['latitude_city'].tolist()
        longitude_city = tab['longitude_city'].tolist()
    
        for z in range(tab.shape[0]) : 
        
            try : 
                continent = get_continent(latitude_city[z], longitude_city[z])
        
                list_pays.append(continent[0])
                list_continent.append(continent[1]) 
                list_lat.append(continent[2])
                list_lon.append(continent[3])
                list_city.append(continent[4])
            except : 
                list_pays.append("None")
                list_continent.append("None")
                list_lat.append("None")
                list_lon.append("None")
                list_city.append("None")
    
        tab["Pays_recod"] = list_pays
        tab["Contient_recod"] = list_continent
        tab["lat_Pays"] = list_lat
        tab["Lon_Pays"] = list_lon
        tab["Ville_recod"] = list_city
    
        
        latitude = []
        longitude = []
        list_continent = []
        list_pays = []
        list_lat = []
        list_lon = []
        list_city = []

        return tab



