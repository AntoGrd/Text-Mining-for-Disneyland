# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:36:08 2022

@author: sibghi
"""

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import time 

url = "https://www.tripadvisor.fr/Attraction_Review-g226865-d189258-Reviews-Disneyland_Paris-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html"

driver = webdriver.Chrome("C:/Users/sibghi/Downloads/chromedriver_win32/chromedriver.exe")

driver.get(url)

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
    blocAvis = soup.find(attrs={"class" : "LbPSX"}) 
    for avis in blocAvis.findAll(attrs={"class" : "C"}):
        
        #Titre commentaire 
        try:
            
            titre = avis.find("span", attrs = {"class": "yCeTE"})
            print(titre.text)
            liste_titre_comm.append(titre.text)
            #print(titre.text)
        except:
            liste_titre_comm.append("None")
    
        #commentaire 
        try:
            
            comment = avis.find(attrs = {"class": "biGQs _P pZUbB KxBGd"})
            liste_comm.append(comment.text)
        except:
            liste_comm.append("None")
    
        #localisation 
        try:
            
            loc = avis.find(attrs = {"class": "JINyA"})
            liste_loc.append(loc.text)
        except:
            liste_loc.append("None")
    
    
        #Note
        try:
            note = avis.find(class_="UctUV d H0")
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









