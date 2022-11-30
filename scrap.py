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
url1 = "https://www.tripadvisor.fr/Attraction_Review-g226865-d189258-Reviews-or"
url2 = "-Disneyland_Paris-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html"
nb = 10

#Titre commentaire 
blocAvis = soup.find(attrs={"class" : "LbPSX"})
for avis in blocAvis.findAll(attrs={"class" : "C"}):
    
    blocAvis = soup.find(attrs={"class" : "LbPSX"})
    titre = avis.find("span", attrs = {"class": "yCeTE"})
    print(titre.text)
    

#commentaire 
for comment in soup.body.find_all(class_="yCeTE"):
    print(comment.text)


#localisation 
for localisation in soup.body.find_all(class_="biGQs _P pZUbB osNWb"):
    print(localisation.text)



###########print("\n\n Présence de photo \n")
for x in soup.body.find_all(class_="ajoIU _S B-"):
    print(x.text)
    
    ###########print("oui")




    driver.find_element(By.CLASS_NAME, "BrOJk u j z _F wSSLS tIqAi unMkR").click()













    driver.find_element(By.XPATH, './/a[@class="BrOJk u j z _F wSSLS tIqAi unMkR"]').click()
    
url_update = url1 + str(nb) + url2 
driver.get(url_update)
    



driver.find_element(By.XPATH, "BrOJk u j z _F wSSLS tIqAi unMkR").click()
driver.find_element("xpath",'//*[@class ="BrOJk u j z _F wSSLS tIqAi unMkR"] /c-wiz/href').click()
