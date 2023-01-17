import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer

def nombre_avis_par_années(df):
  res = df.Annee_Avis.value_counts()
  return res

def répartition_des_notes(df):
  cols = ['b','c','y','orange','r']
  val = df['Note'].value_counts()
  val.plot.pie(autopct='%1.1f%%', shadow= True,colors=cols)
  st.pyplot
  st.set_option('deprecation.showPyplotGlobalUse', False)

def notes(df):
  comptage=df['langue'].value_counts()
  comptage.plot(kind='bar',stacked=True,ylabel="Nombre de répondants",xlabel="Langue de l'avis")
  st.pyplot
  st.set_option('deprecation.showPyplotGlobalUse', False)

def notes1(df):
  T=pd.crosstab(df['langue']=='fr',df['Note'], normalize='index')
  T.plot.barh()
  st.pyplot
  st.set_option('deprecation.showPyplotGlobalUse', False)

def photo_ou_non(df):
  cols = ['b','c','y','orange','r']
  val = df['Photo'].value_counts()
  val.plot.pie(autopct='%1.1f%%', shadow= True,colors=cols)
  st.pyplot
  st.set_option('deprecation.showPyplotGlobalUse', False)

def situation_famille(df):
  cols = ['b','c','y','orange','r']
  val = df['Situation'].value_counts()
  val.plot.pie(autopct='%1.1f%%', shadow= True,colors=cols)
  st.pyplot
  st.set_option('deprecation.showPyplotGlobalUse', False)

def par_pays(df):
  res = df.Pays.value_counts()
  return res
