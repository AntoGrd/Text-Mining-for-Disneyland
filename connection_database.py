import pandas as pd
import mysql.connector
import os
import zipfile

#import tables
os.chdir(r"C:\Documents\travail\LYON2\M2\text_mining\projet_disney\projet_disney\tables")

commentaire=pd.read_csv('tab_commentaire.zip',compression='zip')
date_avis=pd.read_csv("tab_date_avis.csv")
date_sejour=pd.read_csv("tab_date_sejour.csv")
langues=pd.read_csv("tab_langues.csv")
lieux_disney=pd.read_csv("tab_lieux_disney.csv")
note=pd.read_csv("tab_note.csv")
photo=pd.read_csv("tab_photo.csv")
produit=pd.read_csv("tab_produit.csv")
lieu=pd.read_csv("tab_lieu.csv")
situations=pd.read_csv("tab_situations.csv")


lieu.info()

#connection to database
#il faut créer dans db nommée disney_land avant de pouvoir se connecter et ajouter les tables
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

query = f'SET NAMES "utf8mb4"'
cursor.execute(query)
query = f'SET CHARACTER SET utf8mb4'
cursor.execute(query)         
query = f'SET SESSION sql_mode="NO_AUTO_VALUE_ON_ZERO"'
cursor.execute(query)  

#table lieu
table = 'lieu'
query = f'CREATE TABLE {table} (ID_lieu INT PRIMARY KEY, Ville TEXT CHARACTER SET utf8, Pays TEXT CHARACTER SET utf8, Continent TEXT CHARACTER SET utf8)'
cursor.execute(query)

for i, row in lieu.iterrows():
    query = f"INSERT INTO {table} ({','.join(lieu.columns)}) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, tuple(row))
cnx.commit()

#table commentaire
table = 'commentaire'
query = f'CREATE TABLE {table} (ID_commentaire INT PRIMARY KEY, titre_commentaire TEXT CHARACTER SET utf8, commentaire TEXT CHARACTER SET utf8, ID_note INT, ID_photo INT, ID_langue INT, ID_lieux_disney INT, ID_situation INT, ID_produit INT, ID_date_sejour INT, ID_date_avis INT, ID_lieu INT, FOREIGN KEY (ID_note) REFERENCES note(ID_note),FOREIGN KEY (ID_photo) REFERENCES photo(ID_photo),FOREIGN KEY (ID_langue) REFERENCES langues(ID_langue),FOREIGN KEY (ID_lieux_disney) REFERENCES lieux_disney(ID_lieux_disney),FOREIGN KEY (ID_situation) REFERENCES situations(ID_situation),FOREIGN KEY (ID_produit) REFERENCES produit(ID_produit),FOREIGN KEY (ID_date_sejour) REFERENCES date_sejour(ID_date_sejour),FOREIGN KEY (ID_date_avis) REFERENCES date_avis(ID_date_avis),FOREIGN KEY (ID_lieu) REFERENCES lieu(ID_lieu))'

cursor.execute(query)
                                                                                             
for i, row in commentaire.iterrows():
    query = f"INSERT INTO {table} ({','.join(commentaire.columns)}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, tuple(row))
cnx.commit()

cnx.close()








