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

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromdriver")

driver.get(url)

time.sleep(2)
driver.find_element(By.ID,"onetrust-reject-all-handler").click()

content  = driver.page_source
soup = BeautifulSoup(content)

liste_date = []
liste_situation = []
liste_titre_comm  = []
liste_comm = []
liste_loc = []
liste_note = []


blocAvis = soup.find(attrs={"class" : "LbPSX"})
for avis in blocAvis.findAll(attrs={"class" : "C"}):
    
    blocAvis = soup.find(attrs={"class" : "LbPSX"})
    
    #Titre commentaire 
    titre = avis.find("span", attrs = {"class": "yCeTE"})
    liste_titre_comm.append(titre.text)
    #print(titre.text)

    #commentaire 
    comment = avis.find(attrs = {"class": "biGQs _P pZUbB KxBGd"})
    liste_comm.append(comment.text)


    #localisation 
    loc = avis.find(attrs = {"class": "JINyA"})
    liste_loc.append(loc.text)


    #Note
    note = avis.find(class_="UctUV d H0")
    note_clean = note["aria-label"]
    liste_note.append(note_clean)
    

    #situation and date  
    situation = avis.find(class_="RpeCd")
    situation_clean = situation.text
    if "•" in situation_clean:
        liste_sit_date = situation_clean.split("•")
        liste_date.append(liste_sit_date[0])
        liste_situation.append(liste_sit_date[1])
    else:
        liste_date.append(situation.text)



    #next pages after the second page
    driver.find_element(By.CLASS_NAME, "xkSty").click()

    #présence photo 
    #scriptTags = soup.body.find_all(class_="ajoIU _S B-")
    #for script in scriptTags:
        #script_tags = soup.find_all('script', some_attribute=True)
        #print("yes")
    


#scriptTags = soup.findAll(attrs={"class" : "ajoIU _S B-"})
#for script in scriptTags:
    #if script.has_attr('some_attribute'):
      # print('yes')
    #else:
       # print("no")








