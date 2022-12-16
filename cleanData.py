# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

##############file to clean data################

import string
import pandas as pd 
from nltk.tokenize import word_tokenize #pour la tokénisation
import nltk
from nltk.corpus import stopwords
import datetime

ponctuations = set(string.punctuation)
nltk.download('punkt')
nltk.download('stopwords')
mots_vides = stopwords.words("english") + stopwords.words('french')
chiffres = list("0123456789")

def clean_data_hotel(df):
    
    for col in df.columns :
         
        if col == "titre_comm":
            liste_titre_comm = list(df[col].str.lower())
            liste_titre_comm = [w for w in liste_titre_comm if w not in ponctuations]
            liste_titre_comm = [s.replace('...', '') for s in liste_titre_comm]
            liste_titre_comm = [word_tokenize(i) for i in liste_titre_comm]
            #retirer les stopwords
            liste_titre_comm = [w for w in liste_titre_comm if not w in mots_vides]
            #retirer les termes de moins de 3 caractères
            liste_titre_comm = [w for w in liste_titre_comm if len(w)>=3]
            liste_titre_comm = [w for w in liste_titre_comm if not w in chiffres]
        
        if col == "comm":
            liste_comm = list(df[col].str.lower())
            liste_comm = [w for w in liste_comm if w not in ponctuations]
            liste_comm = [s.replace('...', '') for s in liste_comm]
            liste_comm = [word_tokenize(i) for i in liste_comm]
            #retirer les stopwords
            liste_comm = [w for w in liste_comm if not w in mots_vides]
            #retirer les termes de moins de 3 caractères
            liste_comm = [w for w in liste_comm if len(w)>=3]
            liste_titre_comm = [w for w in liste_titre_comm if not w in chiffres]

        if col == "date":
            liste_date = [w.split('(',1)[1] for w in list(df["date"])]
            liste_date = [w.replace(")","") for w in liste_date]
            
            liste_ = []
            for i in liste_date:
                list_split  = i.split(".")
                list_split[0] = "".join([w for w in list_split[0] if not w in chiffres]).replace(" ", "")
                
                
                temp = "".join(list_split)
                temp = temp.split(" ")
                
                if len(temp)==1:
                    temp.append(str(datetime.datetime.now().year))
                
                
                liste_.append(" ".join(temp))
                                
            


            
        if col =="loc":
            
            liste_ville = [item.split(',', 1)[0] for item in list(df[col])]
            liste_Pays = [item.split(',', 1)[1] for item in list(df[col])]
            
        if col == "note":
            list_note = [int(item[7:8]) for item in list(df["note"])]
        
        
    df = pd.DataFrame(list(zip(liste_titre_comm, liste_comm,liste_, liste_ville,liste_Pays, list_note, list(df["photo"]))),
                   columns =['titre_comm', 'comm','date','ville',"pays",'note','photo'])
    
    return df 
    
    

    
    
        


