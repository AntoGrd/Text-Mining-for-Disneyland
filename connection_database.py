import pandas as pd
import mysql.connector
import os

#import tables
os.chdir(r"C:\Documents\travail\LYON2\M2\text_mining\projet_disney\projet_disney\tables")
commentaire=pd.read_csv("tab_commentaire.csv")
date_avis=pd.read_csv("tab_date_avis.csv")
date_sejour=pd.read_csv("tab_date_sejour.csv")
langues=pd.read_csv("tab_langues.csv")
lieux_disney=pd.read_csv("tab_lieux_disney.csv")
note=pd.read_csv("tab_note.csv")
photo=pd.read_csv("tab_photo.csv")
produit=pd.read_csv("tab_produit.csv")
situations=pd.read_csv("tab_situations.csv")

#connection to database
cnx = mysql.connector.connect(user='root',
                              password='root',
                              host='localhost',
                              database='disney_land')
#creation curseur
cursor = cnx.cursor()

#AJOUT DES TABLES

#table date avis
table = 'date_avis'
query = f'CREATE TABLE {table} (ID_date_avis INT PRIMARY KEY, Mois_avis VARCHAR(255), Annee_avis INT)'
cursor.execute(query)

for i, row in date_avis.iterrows():
    query = f"INSERT INTO {table} ({','.join(date_avis.columns)}) VALUES (%s, %s, %s)"
    cursor.execute(query, tuple(row))
cnx.commit()

#table date sejour
table = 'date_sejour'
query = f'CREATE TABLE {table} (ID_date_sejour INT PRIMARY KEY, Mois_sejour VARCHAR(255), Annee_sejour INT)'
cursor.execute(query)

for i, row in date_sejour.iterrows():
    query = f"INSERT INTO {table} ({','.join(date_sejour.columns)}) VALUES (%s, %s, %s)"
    cursor.execute(query, tuple(row))
cnx.commit()

#table langues
table = 'langues'
query = f'CREATE TABLE {table} (ID_langue INT PRIMARY KEY, langue VARCHAR(20))'
cursor.execute(query)

for i, row in langues.iterrows():
    query = f"INSERT INTO {table} ({','.join(langues.columns)}) VALUES (%s, %s)"
    cursor.execute(query, tuple(row))
cnx.commit()

#table lieux_disney
table = 'lieux_disney'
query = f'CREATE TABLE {table} (ID_lieux_disney INT PRIMARY KEY, Lieux_disney VARCHAR(24))'
cursor.execute(query)

for i, row in lieux_disney.iterrows():
    query = f"INSERT INTO {table} ({','.join(lieux_disney.columns)}) VALUES (%s, %s)"
    cursor.execute(query, tuple(row))
cnx.commit()

#table note
table = 'note'
query = f'CREATE TABLE {table} (ID_note INT PRIMARY KEY, Note INT)'
cursor.execute(query)

for i, row in note.iterrows():
    query = f"INSERT INTO {table} ({','.join(note.columns)}) VALUES (%s, %s)"
    cursor.execute(query, tuple(row))
cnx.commit()

#table photo
table = 'photo'
query = f'CREATE TABLE {table} (ID_photo INT PRIMARY KEY, presence_photo VARCHAR(3))'
cursor.execute(query)

for i, row in photo.iterrows():
    query = f"INSERT INTO {table} ({','.join(photo.columns)}) VALUES (%s, %s)"
    cursor.execute(query, tuple(row))
cnx.commit()


#table produit
table = 'produit'
query = f'CREATE TABLE {table} (ID_produit INT PRIMARY KEY, Produit VARCHAR(5))'
cursor.execute(query)

for i, row in produit.iterrows():
    query = f"INSERT INTO {table} ({','.join(produit.columns)}) VALUES (%s, %s)"
    cursor.execute(query, tuple(row))
cnx.commit()


#table situations
table = 'situations'
query = f'CREATE TABLE {table} (ID_situation INT PRIMARY KEY, Situation VARCHAR(18))'
cursor.execute(query)

for i, row in situations.iterrows():
    query = f"INSERT INTO {table} ({','.join(situations.columns)}) VALUES (%s, %s)"
    cursor.execute(query, tuple(row))
cnx.commit()



#table commentaire
table = 'commentaire'
query = f'CREATE TABLE {table} (titre_commentaire VARCHAR(255), commentaire VARCHAR(255), ID_note INT, ID_photo INT, ID_langue INT, ID_lieux_disney INT, ID_situation INT, ID_produit INT, ID_date_sejour INT, ID_date_avis INT)'                                               
cursor.execute(query)

for i, row in commentaire.iterrows():
    query = f"INSERT INTO {table} ({','.join(commentaire.columns)}) VALUES (%s, %s, %s)"
    cursor.execute(query, tuple(row))
cnx.commit()














