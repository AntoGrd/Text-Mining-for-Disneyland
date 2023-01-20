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
import numpy as np

lem = WordNetLemmatizer()
ponctuations = set(string.punctuation)
nltk.download('punkt')
nltk.download('stopwords')
mots_vides_2 = ["marvel","disney","disneyland","hny","new","york","la…","pourtant","car","cependant","toutefois", "néanmoins", "grâce","auron","avon","cela","cet","tout","donc","le…","dès","déjà","bref","jusqu","malgré","ceux","vers","plutôt","etc","tant","entre","puis","leurs","ensuite","afin","parce","estàdire","luimême","sen","quelle","ailleurs","dessus","avoir","oui","newyork","appelle","peuvent","pourraient","littéralement","devenu"]
mots_vides_1 = stopwords.words('french') + mots_vides_2
chiffres = list("0123456789")
mois_debut=['janv','févr','mars','avr','mai','juin','juil','août','sept','oct','nov','déc']
mois_entier=['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre']



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
    #lemmatisation de chaque terme
    doc = [lem.lemmatize(terme) for terme in doc]
    #retirer les stopwords
    doc = [w for w in doc if not w in mots_vides_1]
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

        if col == "dateAvis":
            months=["janv","févr","mars","avr","mai","juin","juil","août","sept","oct","nov","déc"]

            liste_date = [w.split('(',1)[1] for w in list(df[col])]
            liste_date = [w.replace(")","") for w in liste_date]            

            Mois_Avis = []
            Annee_Avis = []
            dateAvis_recod = []
            for i in liste_date: 
                
                #try: 
                if i.find('.') !=-1: 
                    
                    list_split  = i.split(".")
                
                elif i.find(' ') !=-1 : 
                    list_split  = i.split(" ")
                #except:
                else :
                    list_split  = i
                
                if list_split == "Hier":
                        list_split=list_split.replace('Hier',months[datetime.datetime.now().month-1])
                        
                        Mois_Avis.append(list_split)
                        Annee_Avis.append(str(datetime.datetime.now().year))
                        temp = list_split + "," + str(datetime.datetime.now().year)
                        temp  = temp.split(",")
                    
                        dateAvis_recod.append(temp)
                elif list_split == str("Aujourd'hui"):
                        list_split=list_split.replace(str("Aujourd'hui"),months[datetime.datetime.now().month-1])
                        
                        Mois_Avis.append(list_split)
                        Annee_Avis.append(str(datetime.datetime.now().year))
                        temp = list_split + "," + str(datetime.datetime.now().year)
                        temp  = temp.split(",")
                    
                        dateAvis_recod.append(temp)
                else : 
            
                    list_split[0] = "".join([w for w in list_split[0] if not w in chiffres]).replace(" ", "")
                     
                    list_split[1] = list_split[1].replace(" ", "")

                    if list_split[1] == "":
                        
                        list_split[1] = str(datetime.datetime.now().year)
                        
                    Mois_Avis.append(list_split[0])
                    Annee_Avis.append(list_split[1])
                    
                    
                    dateAvis_recod.append(list_split)
                    
                    
            for i in range(len(Mois_Avis)):
                if Mois_Avis[i] in mois_debut :
                    pos = mois_debut.index(Mois_Avis[i])
                    Mois_Avis[i] = Mois_Avis[i].replace(Mois_Avis[i],mois_entier[pos])
                    
            df["dateAvis_recod"] = dateAvis_recod
            df['Mois_Avis'] = Mois_Avis
            df['Annee_Avis'] = Annee_Avis
            
    
        if col == "dateSejour":
                        
            liste_daSej = []
            for i in df["dateSejour"].tolist():
                pos = i.find(":")
                temp = i[pos +2 : len(i)]
                liste_daSej.append(temp)
        
                
            df["dateSejour_recod"] = liste_daSej
            df[['Mois_Sejour','Annee_Sejour']] = df["dateSejour_recod"].str.split(expand=True)

            
        if col =="loc":
            
            liste_ville = [] 
            liste_Pays  = []
            for item in list(df[col]):
                temp = str(item).split(",")
                
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
        
                
    df = pd.DataFrame(list(zip(list(df["titre_comm"]), list(df["comm"]),list(df['Mois_Avis']),list(df['Annee_Avis']), liste_ville,liste_Pays,list(df['Mois_Sejour']),list(df['Annee_Sejour']), list_note, list(df["photo"]), list(df["langue"]))),
                   columns =['titre_commentaire', 'commentaire','Mois_Avis','Annee_Avis','Ville','Pays','Mois_Sejour','Annee_Sejour', 'Note','Photo','langue'])
    return df  

def clean_data_parc(df):    
    
    for col in df.columns :
            
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
                    
        if col == "dateAvis" : 
            
            liste_dateAv = []
            for i in list(df[col]): 
                
                temp = i.split("le ")
                
                if len(temp)==1:
                    liste_dateAv.append("None")
                    
                else : 
                    liste_dateAv.append(temp[1])
            
            liste_Mois_Avis = []
            liste_Annee_Avis = []
            for i in liste_dateAv : 
                
                if i == "None":
                    liste_Mois_Avis.append("None")
                    liste_Annee_Avis.append("None")
                else:
                    temp = i.split(" ")
                    liste_Mois_Avis.append(temp[1])
                    liste_Annee_Avis.append(temp[2])
                    
           
            for i in range(len(liste_Mois_Avis)):
                if liste_Mois_Avis[i] in mois_debut :
                    pos = mois_debut.index(liste_Mois_Avis[i])
                    liste_Mois_Avis[i] = liste_Mois_Avis[i].replace(liste_Mois_Avis[i],mois_entier[pos] )
                
                df["Mois_Avis"] = liste_Mois_Avis
                df["Annee_Avis"] = liste_Annee_Avis
            
                 
        if col == "dateSejour" :
            
                df["dateSejour_recod"] = list(df[col])
                df[['Mois_Sejour','Annee_Sejour']] = df["dateSejour_recod"].str.split(expand=True)
            

        if col == "note":
            list_note = [int(item[0:1]) for item in list(df[col])]
        
        
        df = clean_commentaire(df)
        
    df = pd.DataFrame(list(zip(df["titre_comm"], df["comm"],list(df["Mois_Avis"]), list(df["Annee_Avis"]),list(df["situation"]),liste_ville,liste_Pays, list(df['Mois_Sejour']),list(df['Annee_Sejour']),list_note, list(df["photo"]), list(df["langue"]))),
                   columns =['titre_commentaire', 'commentaire','Mois_Avis','Annee_Avis','Situation','Ville','Pays','Mois_Sejour','Annee_Sejour','Note','Photo','langue'])
    
    return df 


def clean_commentaire(df):
    for col in df.columns :
        if col == "titre_commentaire":
            
            #retrait des ' avant retrait ponctuation pour éviter que les lettres uniques 
            #soient colées avec les mots lors de l'utilisation de nettoyage_corpus
            df[col] = df[col].str.replace("'"," ")
            df[col] = nettoyage_corpus(list(df[col]))
        
        if col == "commentaire":
            
            df[col] = df[col].str.replace("'"," ")
            df[col] = nettoyage_corpus(list(df[col]))
    
    return df
