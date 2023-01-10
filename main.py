import scrap_hotel
import scrap_parc
from selenium import webdriver 
from cleanData import clean_data_hotel, clean_data_parc,clean_commentaire
from traduction import translate
import os
import pandas as pd

url_hotel = ["https://www.tripadvisor.fr/Hotel_Review-g1182377-d262678-Reviews-Disney_Hotel_New_York_The_Art_of_Marvel-Chessy_Marne_la_Vallee_Seine_et_Marne_Ile_de_F.html",
             "https://www.tripadvisor.fr/Hotel_Review-g1182377-d262679-Reviews-Disney_Newport_Bay_Club-Chessy_Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html",
             "https://www.tripadvisor.fr/Hotel_Review-g5599092-d262682-Reviews-Disney_Sequoia_Lodge-Coupvray_Seine_et_Marne_Ile_de_France.html",
             "https://www.tripadvisor.fr/Hotel_Review-g226865-d262686-Reviews-Disney_Hotel_Cheyenne-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html",
             "https://www.tripadvisor.fr/Hotel_Review-g5599092-d262683-Reviews-Disney_Hotel_Santa_Fe-Coupvray_Seine_et_Marne_Ile_de_France.html",
             "https://www.tripadvisor.fr/Hotel_Review-g1221082-d564634-Reviews-Disney_Davy_Crockett_Ranch-Bailly_Romainvilliers_Seine_et_Marne_Ile_de_France.html"]

url_parc = ["https://www.tripadvisor.fr/Attraction_Review-g226865-d189258-Reviews-Disneyland_Paris-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html",
            "https://www.tripadvisor.fr/Attraction_Review-g226865-d285990-Reviews-Walt_Disney_Studios_Park-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html"]


#driver = webdriver.Chrome("C:/Documents/travail/LYON2\M2/text_mining/projet_disney/chromedriver.exe")
#tab=scrap_hotel.scrapping_hotel(url_hotel[0],driver)
#tab = clean_data_hotel(tab)
#tab.to_csv('hotel_marvel.csv', index=False, encoding = 'utf-8-sig')


#Récupération des hotels :
nom_hotels=["hotel_marvel","hotel_newport","hotel_sequoia","hotel_cheyenne", "hotel_sante_fe","hotel_davy_crockett"]
#boucle pour récupérer tous les hotels
for i in range(0,len(url_hotel)): #♠car déjà recup hotel marvel
#for i in len(url_hotel):
    #driver = webdriver.Chrome("C:/Documents/travail/LYON2\M2/text_mining/projet_disney/chromedriver.exe")
    driver = webdriver.Chrome("C:/Users/Sam/Documents/SISE/Text mining/Driver/chromedriver.exe")
    tab=scrap_hotel.scrapping_hotel(url_hotel[i],driver)
            
    #tab = clean_data_hotel(tab)
    tab.to_csv(nom_hotels[i]+'.csv', index=False, encoding = 'utf-8-sig')
   
#Récupération parcs :
namesParc  = ["Disneyland_Paris","Walt_Disney_Studios_Park"]

#boucle pour récupérer tous les parcs
for i in range(0,len(url_parc)):
    #driver = webdriver.Chrome("C:/Documents/travail/LYON2\M2/text_mining/projet_disney/chromedriver.exe")
    driver = webdriver.Chrome("C:/Users/Sam/Documents/SISE/Text mining/Driver/chromedriver.exe")
    tab=scrap_parc.scrapping_parc(url_parc[i],driver)
    #tab = clean_data_parc(tab)
    tab.to_csv(namesParc[i]+'.csv', index=False, encoding = 'utf-8-sig')
    
#traduction et nettoyage des hotels :
#os.chdir(r"C:\Documents\travail\LYON2\M2\text_mining\projet_disney\projet_disney\data")
#tab=pd.read_csv("hotel_marvel.csv")
#os.chdir(r"C:\Documents\travail\LYON2\M2\text_mining\projet_disney\projet_disney")
for i in nom_hotels:
    os.chdir("C:/Users/Sam/Documents/GitHub/Text-Mining-for-Disneyland/data")
    tab=pd.read_csv(str(i) + ".csv")
    os.chdir(r"C:\Users\Sam\Documents\GitHub\Text-Mining-for-Disneyland")
    translate(tab)
    tab = clean_data_hotel(tab)
    tab = clean_commentaire(tab)
    tab.to_csv(str(i) + "_clean.csv", index=False, encoding = 'utf-8-sig')


for i in namesParc:
    os.chdir("C:/Users/Sam/Documents/GitHub/Text-Mining-for-Disneyland/data")
    tab=pd.read_csv(str(i) + ".csv")
    os.chdir(r"C:\Users\Sam\Documents\GitHub\Text-Mining-for-Disneyland")
    translate(tab)
    tab = clean_data_parc(tab)
    tab = clean_commentaire(tab)
    tab.to_csv(str(i) + "_clean.csv", index=False, encoding = 'utf-8-sig')



#ajout de la colonne id 
for i in nom_hotels:
    
    os.chdir("C:/Users/Sam/Documents/GitHub/Text-Mining-for-Disneyland/data")
    tab=pd.read_csv(str(i) + ".csv")
    tab["id"] = tab["dateAvis"] + tab["loc"] +  tab["note"] 
    tab.to_csv(str(i) + ".csv", index=False, encoding = 'utf-8-sig')

for i in namesParc:
    
    os.chdir("C:/Users/Sam/Documents/GitHub/Text-Mining-for-Disneyland/data")
    tab=pd.read_csv(str(i) + ".csv")
    tab["id"] = tab["dateAvis"] + tab["loc"] +  tab["note"] 
    tab.to_csv(str(i) + ".csv", index=False, encoding = 'utf-8-sig')



#test recup nouveau cxommentaire
df = pd.read_csv("hotel_marvel.csv")

driver = webdriver.Chrome("C:/Users/Sam/Documents/SISE/Text mining/Driver/chromedriver.exe")
tab = scrap_hotel.Scraping_NouveauAvis_hotel(url_hotel[0], driver, df)
tab = tab.iloc[:-1,:]
tab.drop_duplicates(keep = 'first', inplace=True)

for z in range(tab.shape[0]):
    for i in range(df.shape[0]):
    
        if(df["id"].tolist()[i] == tab["id"].tolist()[z]) == True:
            tab["id"].tolist().remove(tab["id"].tolist()[z])
        
   

#<<<<<<< HEAD
#namesHotel = ["Hotel_New_York_The_Art_of_Marvel", "Disney_Newport_Bay_Club","Disney_Hotel_Cheyenne","Disney_Davy_Crockett_Ranch"]
#namesParc  = ["Disneyland_Paris","Walt_Disney_Studios_Park"]

#scraping hotel 
#compteurHotel = 0
#for url in url_hotel:

    #tab = scrap_hotel.scrapping_hotel(url,driver)
    #tab = clean_data_hotel(tab)
    #tab.to_csv(namesHotel[namesHotel] + ".csv")
    #compteurHotel += 1

#scraping parc 
#compteurParc = 0
#for url in url_hotel:

    #tab = scrap_parc.scrapping_parc(url,driver)
    #tab = clean_data_parc(tab)
    #tab.to_csv(namesHotel[compteurParc] + ".csv")
    #compteurParc += 1
#=======

#>>>>>>> 7ae12a5be5d37fffcac9fdac4f2e8dddcc4e86b9








