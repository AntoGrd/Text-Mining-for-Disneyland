# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:36:08 2022

@author: sibghi
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 09:39:44 2022

@author: sibghi
"""

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import time 

url = "https://www.tripadvisor.fr/Attraction_Review-g226865-d189258-Reviews-Disneyland_Paris-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html"

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromdriver")

driver.get(url)


driver.find_element(By.ID,"onetrust-reject-all-handler").click()

content  = driver.page_source
soup = BeautifulSoup(content)


#Titre commentaire 
blocAvis = soup.find(attrs={"class" : "LbPSX"})
for avis in blocAvis.findAll(attrs={"class" : "C"}):
    
    blocAvis = soup.find(attrs={"class" : "LbPSX"})
    titre = avis.find("span", attrs = {"class": "yCeTE"})
    print(titre.text)

#commentaire 
for comment in soup.body.find_all(class_="_T FKffI"):
    print(comment.text)


#localisation 
for localisation in soup.body.find_all(class_="JINyA"):
    a = localisation.find("span", attrs = {"class": "mat"})
    print(a.text)

###########print("\n\n PAYS \n")
for x in soup.body.find_all(class_="biGQs _P pZUbB osNWb"):
    print(x.text)

#Note
for note in soup.body.find_all(class_="UctUV d H0"):
    a = note["aria-label"]
    print(a)


#situation de venu 
for situation in soup.body.find_all(class_="RpeCd"):
    print(comment.text)


###########print("\n\n Présence de photo \n")
for x in soup.body.find_all(class_="ajoIU _S B-"):
    
    ###########print("oui")

scriptTags = soup.body.find_all(class_="LblVz _e q")
for script in scriptTags:
    if script.find('button', attrs = {"class": "ajoIU _S B-"}):
        print("oui")
    else:
        print("non")


driver.find_element(By.CLASS_NAME, "BrOJk u j z _F wSSLS tIqAi unMkR").click()








