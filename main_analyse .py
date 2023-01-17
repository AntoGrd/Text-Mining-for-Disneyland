# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 17:25:42 2023

@author: Sam
"""

import fonctions_analyse
from fonctions_analyse import get_continent, add_Sentiment, applyCountry
import pandas as pd
from geopy.geocoders import Nominatim
from tqdm import tqdm
tqdm.pandas()
from dask import delayed      


geolocator  = Nominatim(user_agent = "geoapiExercises")

nom_sites =  ["hotel_sequoia","hotel_cheyenne", "hotel_sante_fe","hotel_davy_crockett","Disneyland_Paris", "Walt_Disney_Studios_Park"]
nom_sites =  ["Disneyland_Paris", "Walt_Disney_Studios_Park"]
   

for i in nom_sites:
    
    y = delayed(applyCountry)("hotel_davy_crockett")
    tab = pd.DataFrame(y.compute())
    
    tab.to_csv("C:/Users/Sam/Documents/GitHub/Text-Mining-for-Disneyland/data_translate/" + "hotel_davy_crockett_ope.csv")
    

import os 
os.chdir("C:/Users/Sam/Documents/GitHub/Text-Mining-for-Disneyland/data_translate")
a = pd.read_csv("hotel_sante_fe_ope.csv")
        