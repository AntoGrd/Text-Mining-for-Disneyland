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
for loc in soup.body.find_all(class_="biGQs _P pZUbB osNWb"):
    print(loc.text)


#Note
for note in soup.body.find_all(class_="UctUV d H0"):
    a = note["aria-label"]
    print(a)


#situation de venu 
for situation in soup.body.find_all(class_="RpeCd"):
    print(situation.text)


#présence photo 
scriptTags = soup.body.find_all(class_="ajoIU _S B-")
for script in scriptTags:
    script_tags = soup.find_all('script', some_attribute=True)
    print("yes")
    


#scriptTags = soup.findAll(attrs={"class" : "ajoIU _S B-"})
#for script in scriptTags:
    #if script.has_attr('some_attribute'):
      # print('yes')
    #else:
       # print("no")

#firt page -> second page
driver.find_element(By.CLASS_NAME, "UCacc").click()

#next pages after the second page
#driver.find_element(By.CSS_SELECTOR, "button.BrOJk u j z _F wSSLS tIqAi iNBVo SSqtP > div.nsTKv").click()








