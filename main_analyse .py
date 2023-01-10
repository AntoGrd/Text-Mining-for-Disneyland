# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 17:25:42 2023

@author: Sam
"""

from fonctions_analyse import get_continent, add_Sentiment, applyCountry
import pandas as pd
from geopy.geocoders import Nominatim
from tqdm import tqdm
tqdm.pandas()
from dask import delayed      


geolocator  = Nominatim(user_agent = "geoapiExercises")

nom_sites =  ["hotel_marvel","hotel_newport","hotel_sequoia","hotel_cheyenne", "hotel_sante_fe","hotel_davy_crockett"]
        

for i in nom_sites:
    
    y = delayed(applyCountry)("hotel_sequoia")
    tab = pd.DataFrame(y.compute())
    
    tab.to_csv("C:/Users/Sam/Documents/GitHub/Text-Mining-for-Disneyland/data_translate/" + "hotel_newport_ope.csv")
    
    
        




