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
import os
def scrapping_hotel(url_hotel, driver):
    
    driver.get(url_hotel)
    
    time.sleep(2)
    driver.find_element(By.ID,"onetrust-reject-all-handler").click()
    time.sleep(1)
    driver.find_element(by=By.CLASS_NAME,value ="Qukvo.Vm._S").click()

    #liste_date = []
    #liste_situation = []
    #liste_sit_date = []
    liste_titre_comm  = []
    liste_comm = []
    liste_loc = []
    liste_note = []
    presence_photo = []
    liste_dateAvis = []
    liste_dateSejour = []
    # boucle pour recuperer les donnees
    #page=1 
    #while(page<4): #juste pour tester
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
              
            #date avis
            try:
                temp = avis.find(attrs = {"cRVSd"})
                dateAvis = temp.find("span").text
                liste_dateAvis.append(dateAvis)
            except:
                liste_dateAvis.append("None, None")
        
            #date sejour 
            try:
                temp = avis.find(attrs = {"class" : "EftBQ"})
                date_sejour = temp.find("span", attrs = {"class" : "teHYY _R Me S4 H3"}).text
                liste_dateSejour.append(date_sejour)
                
            except:
                liste_dateSejour.append("None")
                
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
        #page=page+1
    #fin de la boucle 
    df = pd.DataFrame(list(zip(liste_titre_comm, liste_comm,liste_dateAvis,liste_dateSejour, liste_loc, liste_note, presence_photo)),
                   columns =['titre_comm', 'comm',"dateAvis","dateSejour",'loc','note','photo'])
    return(df)


def Scraping_NouveauAvis_hotel(url_hotel, driver, tab):
    time.sleep(1)
    driver.get(url_hotel)
    
    time.sleep(2)
    driver.find_element(By.ID,"onetrust-reject-all-handler").click()
    time.sleep(1)
    driver.find_element(by=By.CLASS_NAME,value ="Qukvo.Vm._S").click()

    #liste_date = []
    #liste_situation = []
    #liste_sit_date = []
    liste_titre_comm  = []
    liste_comm = []
    liste_loc = []
    liste_note = []
    presence_photo = []
    liste_dateAvis = []
    liste_dateSejour = []
    test_list = []

    # boucle pour recuperer les donnees
    #page=1 
    #while(page<4): #juste pour tester
    compt = 0
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
              
            #date avis
            try:
                temp = avis.find(attrs = {"cRVSd"})
                dateAvis = temp.find("span").text
                liste_dateAvis.append(dateAvis)
            except:
                liste_dateAvis.append("None, None")
        
            #date sejour 
            try:
                temp = avis.find(attrs = {"class" : "EftBQ"})
                date_sejour = temp.find("span", attrs = {"class" : "teHYY _R Me S4 H3"}).text
                liste_dateSejour.append(date_sejour)
                
            except:
                liste_dateSejour.append("None")
                
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
                
            
            test = liste_dateAvis[compt] + liste_loc[compt] + liste_note[compt]
            test_list.append(test)
            if test in tab["id"].to_list():
                accord = True
            else:
                accord = False
                compt +=1  
        
       
        time.sleep(2)
        
        if accord == True:
            driver.quit()
            break
        else:
            driver.find_element(by=By.CSS_SELECTOR, value='.ui_button.nav.next.primary').click()
    
        #page=page+1
    #fin de la boucle 
    df = pd.DataFrame(list(zip(liste_titre_comm, liste_comm,liste_dateAvis,liste_dateSejour, liste_loc, liste_note, presence_photo, test_list)),
                   columns =['titre_comm', 'comm',"dateAvis","dateSejour",'loc','note','photo', 'id'])
    
    df = df.iloc[:-1,:]
    df.drop_duplicates(keep = 'first', inplace=True)

    for z in range(df.shape[0]):
        for i in range(tab.shape[0]):
        
            if(tab["id"].tolist()[i] == df["id"].tolist()[z]) == True:
                df["id"].tolist().remove(df["id"].tolist()[z])
    return(df)
