# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

##############file to clean data################

import string
import pandas as pd 
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize #pour la tokénisation
import nltk
from nltk.corpus import stopwords
import datetime

lem = WordNetLemmatizer()
ponctuations = set(string.punctuation)
nltk.download('punkt')
nltk.download('stopwords')
mots_vides = stopwords.words("english") + stopwords.words('french')
chiffres = list("0123456789")


def nettoyage_doc(doc_param):
    #passage en minuscule
    doc = doc_param.lower()
    #doc = " ".join([w for w in list(doc) if not w in "'"])
    #retrait des ponctuations
    doc = "".join([w for w in list(doc) if not w in ponctuations])
    #retirer les chiffres
    doc = "".join([w for w in list(doc) if not w in chiffres])
    #transformer le document en liste de termes par tokénisation
    doc = word_tokenize(doc)
    #lematisation de chaque terme
    doc = [lem.lemmatize(terme) for terme in doc]
    #retirer les stopwords
    doc = [w for w in doc if not w in mots_vides]
    #retirer les termes de moins de 3 caractères
    doc = [w for w in doc if len(w)>=3]
    #fin
    return doc

#************************************************************
#fonction pour nettoyage corpus
#attention, optionnellement les documents vides sont éliminés
#************************************************************
def nettoyage_corpus(corpus,vire_vide=True):
    #output
    output = [nettoyage_doc(doc) for doc in corpus if ((len(doc) > 0) or (vire_vide == False))]
    return output



def clean_data_hotel(df):
    
    for col in df.columns :
         
        if col == "titre_comm":
            #retrait des ' avant retrait ponctuation pour éviter que les lettres uniques 
            #soient colées avec les mots lors de l'utilisation de nettoyage_corpus
            df[col] = df[col].str.replace("'"," ")
            liste_titre_comm = nettoyage_corpus(list(df[col]))
        
        if col == "comm":
            df[col] = df[col].str.replace("'"," ")
            liste_comm = nettoyage_corpus(list(df[col]))

        if col == "date":
            liste_date = [w.split('(',1)[1] for w in list(df[col])]
            liste_date = [w.replace(")","") for w in liste_date]
            
            liste_ = []
            for i in liste_date:
                list_split  = i.split(".")
                list_split[0] = "".join([w for w in list_split[0] if not w in chiffres]).replace(" ", "")
                
                
                temp = "".join(list_split)
                temp = temp.split(" ")
                
                if len(temp)==1:
                    temp.append(str(datetime.datetime.now().year))
                
                date=(" ".join(temp))
                months=["janv","févr","mars","avr","mai","juin","juil","août","sept","oct","nov","déc"]
                if "Hier" in date:
                    date=date.replace('Hier',months[datetime.datetime.now().month-1])    
                liste_.append(date)
                

        if col =="loc":
            
            liste_ville = [] 
            liste_Pays  = []
            for item in list(df[col]):
                temp = item.split(",")
                
                try:
                    liste_ville.append(temp[0])
                except:
                    
                    liste_ville.append("None")
                try:
                    liste_Pays.append(temp[1])
                except:
                    
                    liste_Pays.append("None")
            
        if col == "note":
            list_note = [int(item[7:8]) for item in list(df[col])]
        
        
    df = pd.DataFrame(list(zip(liste_titre_comm, liste_comm,liste_, liste_ville,liste_Pays, list_note, list(df["photo"]), list(df["langue"]))),
                   columns =['titre_commentaire', 'commentaire','Date','Ville','Pays','Note','Photo','langue'])
    
    return df 
    

def clean_data_parc(df):    
    
    for col in df.columns :
         
        if col == "titre_comm":
            
            #retrait des ' avant retrait ponctuation pour éviter que les lettres uniques 
            #soient colées avec les mots lors de l'utilisation de nettoyage_corpus
            df[col] = df[col].str.replace("'"," ")
            liste_titre_comm = nettoyage_corpus(list(df[col]))
        
        if col == "comm":
            
            df[col] = df[col].str.replace("'"," ")
            liste_comm = nettoyage_corpus(list(df[col]))

        if col =="loc":
            
            liste_loc = []
            for item in list(df[col]):
                
                if item[0][0] in chiffres:
                    liste_loc.append("None, None")
                else:
                    liste_loc.append(item)
                 
            liste_ville = [] 
            liste_Pays  = []
            for item in liste_loc:
                temp = item.split(",")
                
                try:
                    liste_ville.append(temp[0])
                except:
                    
                    liste_ville.append("None")
                try:
                    liste_Pays.append(temp[1])
                except:
                    
                    liste_Pays.append("None")
                    
            
        if col == "note":
            list_note = [int(item[0:1]) for item in list(df[col])]
        
        
    df = pd.DataFrame(list(zip(liste_titre_comm, liste_comm,list(df["date"]), list(df["situation"]),liste_ville,liste_Pays, list_note, list(df["photo"]), list(df["langue"]))),
                   columns =['titre_commentaire', 'commentaire','Date','Situation','Ville',"Pays","Note",'Photo'])
    
    return df 