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

