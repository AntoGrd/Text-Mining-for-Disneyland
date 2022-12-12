# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 21:57:18 2022

@author: Sam
"""

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import time 

url_hotel = ["https://www.tripadvisor.fr/Hotel_Review-g1182377-d262678-Reviews-Disney_Hotel_New_York_The_Art_of_Marvel-Chessy_Marne_la_Vallee_Seine_et_Marne_Ile_de_F.html",
             "https://www.tripadvisor.fr/Hotel_Review-g1182377-d262679-Reviews-Disney_Newport_Bay_Club-Chessy_Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html",
             "https://www.tripadvisor.fr/Hotel_Review-g5599092-d262682-Reviews-Disney_Sequoia_Lodge-Coupvray_Seine_et_Marne_Ile_de_France.html",
             "https://www.tripadvisor.fr/Hotel_Review-g226865-d262686-Reviews-Disney_Hotel_Cheyenne-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html",
             "https://www.tripadvisor.fr/Hotel_Review-g5599092-d262683-Reviews-Disney_Hotel_Santa_Fe-Coupvray_Seine_et_Marne_Ile_de_France.html",
             "https://www.tripadvisor.fr/Hotel_Review-g1221082-d564634-Reviews-Disney_Davy_Crockett_Ranch-Bailly_Romainvilliers_Seine_et_Marne_Ile_de_France.html"]


driver = webdriver.Chrome("C:/Users/Sam/Documents/SISE/Text mining/Driver/chromedriver.exe")

driver.get(url_hotel[0])

time.sleep(2)
driver.find_element(By.ID,"onetrust-reject-all-handler").click()



liste_date = []
liste_situation = []
liste_sit_date = []
liste_titre_comm  = []
liste_comm = []
liste_loc = []
liste_note = []
presence_photo = []

# boucle pour recuperer les donnees
while(True) :
    
    time.sleep(2)
    content  = driver.page_source
    soup = BeautifulSoup(content)
    for avis in soup.findAll("div", {'class':'YibKl MC R2 Gi z Z BB pBbQr'}):
        
        #Titre commentaire 
        try:
            titre = avis.find(attrs = {"class": "KgQgP MC _S b S6 H5 _a"})
            liste_titre_comm.append(titre.text)
            #print(titre.text)
        except:
            liste_titre_comm.append("None")

        #commentaire 
        try:
            
            comment = avis.find(attrs = {"class": "fIrGe _T"})
            liste_comm.append(comment.text)
        except:
            liste_comm.append("None")
    
        #localisation 
        try:
            
            loc = avis.find(attrs = {"class": "MziKN"})
            loc_precise = loc.find("span", attrs = {"class": "ui_icon map-pin-fill fXexN"})
            liste_loc.append(loc_precise.text)
        except:
            liste_loc.append("None")
    
    
        #Note
        try:
            note = avis.find("div", attrs = {"class": "IkECb f O"})
            note.find("span", attrs = {"class": "ui_bubble_rating bubble_50"}).text
            note_clean = note["aria-label"]
            liste_note.append(note_clean)
        except:
            liste_note.append("None")
        
    
        #situation and date
        #on utlise try pour eviter la non presence de balises 
        try:
            situation = avis.find(attrs = {"class": "RpeCd"})
        
            liste_sit_date.append(situation.text)
            
            if "•" in liste_sit_date[0]:
                liste_temp = liste_sit_date[0].split("•")
                liste_date.append(liste_temp[0])
                liste_situation.append(liste_temp[1])
            else:
                liste_date.append(liste_sit_date[0])
        except:
            liste_date.append("None")
            liste_situation.append("None")
            
        liste_sit_date = []
        
        #test presence photo 
        try:
            photo = avis.find(attrs = {"class" : "ajoIU _S B-"})
            if (photo.name =="button"):
               presence_photo.append("yes")
        except:
            presence_photo.append("no")
    
    
    try:
        driver.find_element(By.CLASS_NAME, "xkSty").click()
    except:
        
        driver.quit()
    
#fin de la boucle 