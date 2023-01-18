import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import wordcloud as wc
import plotly.graph_objs as go

def nombre_avis_par_années(df):
  res = df.Annee_Avis.value_counts()
  return res

def répartition_des_notes(df):
  cols = df['Note']
  val = df['Note'].value_counts()
  fig = go.Figure(data=[go.Pie(labels = cols, values = val)])
  return fig

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
  cols = df['Photo']
  val = df['Photo'].value_counts()
  fig = go.Figure(data=[go.Pie(labels = cols, values = val)])
  return fig

def situation_famille(df):
  cols = df['Situation']
  val = df['Situation'].value_counts()
  fig = go.Figure(data=[go.Pie(labels = cols, values = val)])
  return fig

def par_pays(df):
  res = df.Pays.value_counts()
  return res

def nuage_de_mots(df):
  data = df.commentaire
  wordCloud = wc.WordCloud(background_color="white", width=800, height=600, max_words=100).generate(str(data))
  plt.imshow(wordCloud, interpolation="bilinear")
  plt.axis('off')
  st.pyplot()
