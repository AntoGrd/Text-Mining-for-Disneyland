import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

def nombre_avis_par_années(df):
  print(df.Annee_Avis.value_counts())
 

def répartition_des_notes(df):
  plt.figure(figsize=(6, 6))
  cols = ['b','c','y','orange','r']
  df['Note'].value_counts().plot.pie(autopct='%1.1f%%', shadow= True,colors=cols)
  plt.show()

def notes(df):
  comptage=df['langue'].value_counts()
  comptage.plot(kind='bar',stacked=True,ylabel="Nombre de répondants",xlabel="Langue de l'avis")
  T=pd.crosstab(df['langue']=='fr',df['Note'], normalize='index')
  T.plot.barh()
  plt.show()

