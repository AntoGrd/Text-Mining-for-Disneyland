import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer

def nombre_avis_par_années(df):
  df.Annee_Avis.value_counts()
  st.write

def répartition_des_notes(df):
  cols = ['b','c','y','orange','r']
  val = df['Note'].value_counts()
  val.plot.pie(autopct='%1.1f%%', shadow= True,colors=cols)
  st.pyplot

def notes(df):
  comptage=df['langue'].value_counts()
  comptage.plot(kind='bar',stacked=True,ylabel="Nombre de répondants",xlabel="Langue de l'avis")
  st.pyplot

def notes1(df):
  T=pd.crosstab(df['langue']=='fr',df['Note'], normalize='index')
  T.plot.barh()
  st.pyplot
