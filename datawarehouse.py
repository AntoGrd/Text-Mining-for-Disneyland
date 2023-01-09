import os
import pandas as pd
import numpy as np
from cleanData import clean_data_hotel, clean_data_parc

os.chdir(r"C:\Documents\travail\LYON2\M2\text_mining\projet_disney\projet_disney\data_translate")
#os.chdir(r"C:\Documents\travail\LYON2\M2\text_mining\projet_disney\projet_disney\tables")
#tab_commentaire=pd.read_csv("tab_commentaire.csv")

tab=pd.read_csv("hotel_cheyenne_fr.csv")
tab2=pd.read_csv("hotel_davy_crockett_fr.csv")  
tab3=pd.read_csv("hotel_marvel_fr.csv")
tab4=pd.read_csv("hotel_newport_fr.csv")
tab5=pd.read_csv("hotel_sante_fe_fr.csv")
tab6=pd.read_csv("hotel_sequoia_fr.csv")

tab7=pd.read_csv("Disneyland_Paris_fr_debut.csv")
tab8=pd.read_csv("Walt_Disney_Studios_Park_fr_debut.csv")

tab = clean_data_hotel(tab)
tab2 = clean_data_hotel(tab2)
tab3 = clean_data_hotel(tab3)
tab4 = clean_data_hotel(tab4)
tab5 = clean_data_hotel(tab5)
tab6 = clean_data_hotel(tab6)
tab7 = clean_data_parc(tab7)
tab8 = clean_data_parc(tab8)
tab.info()


#je vire les avis avec pintade et Rachaécritunavis(févr 
#à intégrer dans les df
#tab['Mois_Avis'].value_counts()
#tab6['Mois_Avis'].value_counts()
#tab['Mois_Avis']=="Rachaécritunavis(févr"

#tab.loc[(tab['Mois_Avis']=="Rachaécritunavis(févr"),:]
tab=tab.drop(254)
#tab6.loc[(tab6['Mois_Avis']=="Pintade"),:]
tab6=tab6.drop(10414)


liste_tab_hotels=[tab,tab2,tab3,tab4,tab5,tab6]
liste_tab_parcs=[tab7,tab8]
#Creation des tables

#table Lieux_disney
lieux_disney=["hotel_cheyenne","hotel_davy_crockett","hotel_marvel","hotel_newport","hotel_sante_fe","hotel_sequoia","Disneyland_Paris","Walt_Disney_Studios_Park"]
tab_lieux_disney=pd.DataFrame({'ID_lieux_disney':[1,2,3,4,5,6,7,8],'Lieux_disney':lieux_disney})

#Réunir les hotels et parcs
liste_lieux_hotels=[]
for i in range(0,len(liste_tab_hotels)):
    liste_lieux_hotels.extend([lieux_disney[i]]*len(liste_tab_hotels[i]))
    
liste_lieux_parcs=[]   
for i in range(0,len(liste_tab_parcs)):
     liste_lieux_parcs.extend([lieux_disney[i+len(liste_tab_hotels)]]*len(liste_tab_parcs[i])) 

#années en float > passer en integer
for i in range(0,len(liste_tab_hotels)):
    liste_tab_hotels[i]['Annee_Sejour']=liste_tab_hotels[i]['Annee_Sejour'].replace(np.nan, 0)
    liste_tab_hotels[i]['Annee_Sejour']=liste_tab_hotels[i]['Annee_Sejour'].astype(int)

for i in range(0,len(liste_tab_parcs)):
    liste_tab_parcs[i]['Annee_Avis']=liste_tab_parcs[i]['Annee_Avis'].replace("None", 0)
    liste_tab_parcs[i]['Annee_Avis']=liste_tab_parcs[i]['Annee_Avis'].astype(int)
    
#liste_tab_parcs[0]['Annee_Avis']=liste_tab_hotels[1]['Annee_Avis'].astype(int)
#liste_tab_parcs[1]['Annee_Avis']=liste_tab_hotels[1]['Annee_Avis'].astype(int)
#liste_tab_parcs[1]['Annee_Avis'].value_counts()   
#liste_tab_parcs[1].info()

parcs=pd.concat([tab7,tab8])
parcs.insert(12,"Nom",liste_lieux_parcs)

hotels=pd.concat([tab,tab2,tab3,tab4,tab5,tab6],ignore_index=True)
hotels.insert(11,"Nom",liste_lieux_hotels)

#table Notes
tab_note=pd.DataFrame({'ID_note':[1,2,3,4,5],'Note':[1,2,3,4,5]})

#table Types
tab_type=pd.DataFrame({'ID_produit':[1,2],'Produit':["Hotel","Parc"]})

#table Situations
tab_situations=pd.DataFrame({'ID_situation':[1,2,3,4,5,6],'Situation':[" Entre amis"," En famille"," En couple","None"," Voyage d'affaires"," En solo"]})

#table Présence photos
tab_photo=pd.DataFrame({'ID_photo':[1,2],'presence_photo':['yes','no']})

#table Langue
tab_langues=[*hotels["langue"],*parcs["langue"]]
tab_langues=pd.DataFrame(list(set(tab_langues)),columns = ['langue'])
tab_langues.insert(0,'ID_langue',range(1,1+len(tab_langues)))

#table Date_avis
#A revoir : années entre parc et hotel en double jsp pk

tabma=pd.DataFrame([*hotels["Mois_Avis"],*parcs["Mois_Avis"]])
tabaa=pd.DataFrame([*hotels["Annee_Avis"],*parcs["Annee_Avis"]])

#mois_entier=['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre']
#mois_debut=['janv','févr','mars','avr','mai','juin','juil','août','sept','oct','nov','déc']
#tabma = tabma.replace(mois_debut,mois_entier)

tab_date_avis=pd.DataFrame({'Mois_avis':tabma[0],'Annee_avis':tabaa[0]})
tab_date_avis.drop_duplicates(keep = 'first', inplace=True)
tab_date_avis.insert(0,'ID_date_avis',range(1,1+len(tab_date_avis)))

tab_date_avis['Mois_avis'].value_counts()

#hotels["Annee_Avis"].dtypes
#parcs["Annee_Avis"].value_counts()
#len(parcs["Annee_Avis"])

#tab_date_avis.value_counts()
#tab_date_avis['Annee_avis'].dtypes
#tab_date_avis.iloc[6,:]==tab_date_avis.iloc[148,:]
#tab_date_avis.iloc[6,1].dtypes
#table Date_sejour
#il y a un commentaire où mois = one (supprimer l'avis ?) (peut etre un None ?) 
hotels['Annee_Sejour']=hotels['Annee_Sejour'].replace(np.nan, 0)
hotels['Annee_Sejour']=hotels['Annee_Sejour'].astype(int)
hotels['Mois_Sejour'][hotels['Mois_Sejour']=="one"]="None"
parcs['Annee_Sejour']=parcs['Annee_Sejour'].replace(np.nan, 0)
parcs['Annee_Sejour']=parcs['Annee_Sejour'].astype(int)
#parcs['Mois_Sejour'][parcs['Mois_Sejour']=="None"]=0  

tabms=pd.DataFrame([*hotels["Mois_Sejour"],*parcs["Mois_Sejour"]])
tabas=pd.DataFrame([*hotels["Annee_Sejour"],*parcs["Annee_Sejour"]])
mois_entier=['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre']
mois_debut2=['janv.','févr.','mars','avr.','mai','juin','juil.','août','sept.','oct.','nov.','déc.']
tabms = tabms.replace(mois_debut2,mois_entier)

tab_date_sejour=pd.DataFrame({'Mois_sejour':tabms[0],'Annee_sejour':tabas[0]})
tab_date_sejour.drop_duplicates(keep = 'first', inplace=True)
tab_date_sejour.insert(0,'ID_date_sejour',range(1,1+len(tab_date_sejour)))
tab_date_sejour['Annee_sejour'].value_counts()

#Lieux (pour l'instant je laisse de côté)
tabp=[*hotels["Pays"],*parcs["Pays"]]
tabp=list(set(tabp))
tabv=[*hotels["Ville"],*parcs["Ville"]]
tabv=list(set(tabv))


###Création table commentaire
tab_commentaire=pd.concat([hotels,parcs]).reset_index(drop=True)
tab_commentaire["Situation"]=tab_commentaire["Situation"].replace(np.nan,"None")
liste_type=[]
liste_type.extend([tab_type["Produit"][0]]*len(hotels))
liste_type.extend([tab_type["Produit"][1]]*len(parcs))
tab_commentaire["Produit"]=liste_type

tab_commentaire["Note"]=tab_commentaire["Note"].replace(tab_note['Note'].values.tolist(),tab_note['ID_note'].values.tolist())
tab_commentaire["Photo"]=tab_commentaire["Photo"].replace(tab_photo['presence_photo'].values.tolist(),tab_photo['ID_photo'].values.tolist())
tab_commentaire["langue"]=tab_commentaire["langue"].replace(tab_langues['langue'].values.tolist(),tab_langues['ID_langue'].values.tolist())
tab_commentaire["Situation"]=tab_commentaire["Situation"].replace(tab_situations['Situation'].values.tolist(),tab_situations['ID_situation'].values.tolist())
tab_commentaire["Nom"]=tab_commentaire["Nom"].replace(tab_lieux_disney['Lieux_disney'].values.tolist(),tab_lieux_disney['ID_lieux_disney'].values.tolist())
tab_commentaire["Produit"]=tab_commentaire["Produit"].replace(tab_type['Produit'].values.tolist(),tab_type['ID_produit'].values.tolist())

#tab_commentaire['Mois_Avis']=tab_commentaire['Mois_Avis'].replace(mois_debut,mois_entier)
tab_commentaire['Date_avis']=tab_commentaire['Mois_Avis']+tab_commentaire['Annee_Avis'].apply(str)
date_avis=tab_date_avis['Mois_avis']+tab_date_avis['Annee_avis'].apply(str)
tab_commentaire['Date_avis']=tab_commentaire["Date_avis"].replace(date_avis.values.tolist(),tab_date_avis["ID_date_avis"].values.tolist())

tab_commentaire['Mois_Sejour']=tab_commentaire['Mois_Sejour'].replace(mois_debut2,mois_entier)
tab_commentaire['Date_Sejour']=tab_commentaire['Mois_Sejour']+tab_commentaire['Annee_Sejour'].apply(str)
date_sejour=tab_date_sejour['Mois_sejour']+tab_date_sejour['Annee_sejour'].apply(str)
tab_commentaire['Date_Sejour']=tab_commentaire["Date_Sejour"].replace(date_sejour.values.tolist(),tab_date_sejour["ID_date_sejour"].values.tolist())

tab_commentaire=tab_commentaire.drop(['Mois_Avis','Annee_Avis','Mois_Sejour','Annee_Sejour'], axis=1)
tab_commentaire=tab_commentaire.drop(['Ville','Pays'], axis=1) #temporairement

tab_commentaire.insert(0,'ID_commentaire',range(1,1+len(tab_commentaire)))

print(tab_commentaire.columns.values)
tab_commentaire.set_axis(['ID_commentaire','titre_commentaire', 'commentaire', 'ID_note','ID_photo','ID_langue','ID_lieux_disney','ID_situation','ID_produit','ID_date_sejour','ID_date_avis'], axis='columns', inplace=True)

os.chdir(r"C:\Documents\travail\LYON2\M2\text_mining\projet_disney\projet_disney\tables")
tab_commentaire.to_csv('tab_commentaire.csv', index=False, encoding = 'utf-8-sig')
tab_note.to_csv('tab_note.csv', index=False, encoding = 'utf-8-sig')
tab_photo.to_csv('tab_photo.csv', index=False, encoding = 'utf-8-sig')
tab_langues.to_csv('tab_langues.csv', index=False, encoding = 'utf-8-sig')
tab_situations.to_csv('tab_situations.csv', index=False, encoding = 'utf-8-sig')
tab_lieux_disney.to_csv('tab_lieux_disney.csv', index=False, encoding = 'utf-8-sig')
tab_type.to_csv('tab_produit.csv', index=False, encoding = 'utf-8-sig')
tab_date_avis.to_csv('tab_date_avis.csv', index=False, encoding = 'utf-8-sig')
tab_date_sejour.to_csv('tab_date_sejour.csv', index=False, encoding = 'utf-8-sig')





