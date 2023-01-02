import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

parcDisney = pd.read_csv("/content/Disneyland_Paris_clean.csv", sep=",")
parcDisney.info( )

studio = pd.read_csv("/content/Walt_Disney_Studios_Park_clean.csv", sep = ',')
studio.info()

def nombre_avis_par_années(df):
  print(df.Annee_Avis.value_counts())
 
nombre_avis_par_années(parcDisney)
nombre_avis_par_années(studio)

def répartition_des_notes(df):
  plt.figure(figsize=(6, 6))
  cols = ['b','c','y','orange','r']
  df['Note'].value_counts().plot.pie(autopct='%1.1f%%', shadow= True,colors=cols)
  plt.show()

répartition_des_notes(studio)
répartition_des_notes(parcDisney)

def notes(df):
  comptage=df['langue'].value_counts()
  comptage.plot(kind='bar',stacked=True,ylabel="Nombre de répondants",xlabel="Langue de l'avis")
  T=pd.crosstab(df['langue']=='fr',df['Note'], normalize='index')
  T.plot.barh()
  plt.show()

notes(parcDisney)
notes(studio)

