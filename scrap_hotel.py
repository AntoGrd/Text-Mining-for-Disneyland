# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 21:57:18 2022
@author: Sam
"""

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import time 
import pandas as pd

def scrapping_hotel(url_hotel, driver):
    
    driver.get(url_hotel)
    
    time.sleep(2)
    driver.find_element(By.ID,"onetrust-reject-all-handler").click()
    
    #liste_date = []
    #liste_situation = []
    #liste_sit_date = []
    liste_titre_comm  = []
    liste_comm = []
    liste_loc = []
    liste_note = []
    presence_photo = []
    liste_date = []
    # boucle pour recuperer les donnees
    page=1 
    while(page<4): #juste pour tester
    #while(True) :
        
        
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
                
            try:
                temp = avis.find(attrs = {"cRVSd"})
                date = temp.find("span").text
                liste_date.append(date)
            except:
                liste_date.append("None, None")
        
            #localisation 
            try:
                
                loc = avis.find(attrs = {"class": "MziKN"})
                loc_precise = loc.find("span", attrs = {"class": "default LXUOn small"})
                liste_loc.append(loc_precise.text)
            except:
                liste_loc.append("None, None")
        
        
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
            break
        page=page+1
    #fin de la boucle 
    df = pd.DataFrame(list(zip(liste_titre_comm, liste_comm,liste_date, liste_loc, liste_note, presence_photo)),
                   columns =['titre_comm', 'comm',"date",'loc','note','photo'])
    return(df)








