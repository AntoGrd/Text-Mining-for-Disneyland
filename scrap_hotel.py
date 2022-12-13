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
            loc_precise = loc.find("span", attrs = {"class": "default LXUOn small"})
            liste_loc.append(loc_precise.text)
        except:
            liste_loc.append("None")
    
    
        #Note
        try:
            note = avis.find("div", attrs = {"class": "IkECb f O"})
            search_span = note.find("div", attrs = {"class": "Hlmiy F1"})
            res = search_span.find("span")
            if res.has_attr('class'):
                
                note_clean = res['class'][1]
            
            liste_note.append(note_clean)
            
        except:
            liste_note.append("None")
        
        #test presence photo 
        try:
            
            photo = avis.find("div", attrs = {"class" : "BSBvb GA"})
            if (photo is not None):
               presence_photo.append("yes")
            else:
    
                presence_photo.append("no")
        except:
            
            presence_photo.append("no")
    
    time.sleep(2)
    try:
        driver.find_element(by=By.CSS_SELECTOR, value='.ui_button.nav.next.primary').click()
    except:
        
        driver.quit()
    
#fin de la boucle 