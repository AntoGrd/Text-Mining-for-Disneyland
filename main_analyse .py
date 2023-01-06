# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 17:25:42 2023

@author: Sam
"""

import fonctions_analyse
import pandas as pd
import os
from geopy.geocoders import Nominatim
from tqdm import tqdm
tqdm.pandas()


geolocator  = Nominatim(user_agent = "geoapiExercises")


latitude = []
longitude = []
list_continent = []
list_pays = []
list_lat = []
list_lon = []

nom_sites =  ["Disneyland_Paris","Walt_Disney_Studios_Park","hotel_marvel",
              "hotel_newport","hotel_sequoia","hotel_cheyenne", "hotel_sante_fe","hotel_davy_crockett"]

for i in nom_sites:
    
    os.chdir("C:/Users/Sam/Documents/GitHub/Text-Mining-for-Disneyland/data_clean")
    tab=pd.read_csv(str(i) + "_clean.csv")
    
    d_sentiment = fonctions_analyse.add_Sentiment(tab) #ajouter la colonne sentiment sur les commentaires
    
    #ajouter la lattitude et longitudes des villes 
    for ville in d_sentiment['Ville'] : 
    
        try :
            location = geolocator.geocode(str(ville))
            latitude.append(location.latitude)
    
            longitude.append(location.longitude)
    
        except :
        
            latitude.append("None")
    
            longitude.append("None")
        
    
    d_sentiment['latitude_city'] = latitude

    d_sentiment['longitude_city'] = longitude

    latitude_city = d_sentiment['latitude_city'].tolist()
    longitude_city = d_sentiment['longitude_city'].tolist()

    for z in range(d_sentiment.shape[0]) : 
    
        try : 
            continent = fonctions_analyse.get_continent(latitude_city[z], longitude_city[z])
    
            list_pays.append(continent[0])
            list_continent.append(continent[1])
            list_lat.append(continent[2])
            list_lon.append(continent[3])
        except : 
            list_pays.append("None")
            list_continent.append("None")
            list_lat.append("None")
            list_lon.append("None")

    d_sentiment["Pays_recod"] = list_pays
    d_sentiment["Contient_recod"] = list_continent
    d_sentiment["lat_Pays"] = list_lat
    d_sentiment["Lon_Pays"] = list_lon
    
    
    d_sentiment.to_csv(str(i) + "_ope.csv", index=False, encoding = 'utf-8-sig')




    