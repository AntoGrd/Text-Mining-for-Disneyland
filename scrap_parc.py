from selenium import webdriver 
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import time 
import pandas as pd

def scrapping_parc(url_parc, driver):
    
    driver.get(url_parc)
    
    time.sleep(2)
    driver.find_element(By.ID,"onetrust-reject-all-handler").click()
    
    time.sleep(1)
    driver.find_element(By.CLASS_NAME,"NK").click()
    time.sleep(1)
    driver.find_element(By.ID,"menu-item-all").click()
    
    liste_dateAvis = []
    liste_situation = []
    liste_sit_date = []
    liste_titre_comm  = []
    liste_comm = []
    liste_loc = []
    liste_note = []
    presence_photo = []
    liste_dateSejour = []
    
    # boucle pour recuperer les donnees
        #while(True) :
    #page=1 
    #while(page<2): #juste pour tester
    while(True) :    
        
        time.sleep(3)
        content  = driver.page_source
        soup = BeautifulSoup(content,features="lxml")
        blocAvis = soup.find(attrs={"class" : "LbPSX"}) 
        for avis in blocAvis.findAll(attrs={"class" : "C"}):
            
            #Titre commentaire 
            try:
                
                titre = avis.find("span", attrs = {"class": "yCeTE"})
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
                
                temp = avis.find(attrs = {"class": "JINyA"})
                loc = temp.find("span").text
                liste_loc.append(loc)
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
                    liste_dateSejour.append(liste_temp[0])
                    liste_situation.append(liste_temp[1])
                else:
                    liste_dateSejour.append(liste_sit_date[0])
            except:
                liste_dateSejour.append("None")
                liste_situation.append("None")
                
            liste_sit_date = []
            
            try:
                dateAvis = avis.find(attrs = {"class": "biGQs _P pZUbB xUqsL ncFvv osNWb"}).text
                liste_dateAvis.append(dateAvis)
            except:
                liste_dateAvis.append("None")
            
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
            break
        #page=page+1    
        
    #fin de la boucle 
    df = pd.DataFrame(list(zip(liste_dateSejour, liste_situation, liste_titre_comm, liste_comm, liste_loc,liste_dateAvis, liste_note, presence_photo)),
                   columns =['dateSejour','situation','titre_comm', 'comm','loc','dateAvis','note','photo'])
    return(df)











