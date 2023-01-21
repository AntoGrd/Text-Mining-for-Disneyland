import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import wordcloud as wc
import plotly.graph_objs as go

def nombre_avis_par_années(df):
  res = df.Annee_avis.value_counts()
  return res

def répartition_des_notes(df):
  cols = df['Note'].unique()
  val = df['Note'].value_counts()
  fig = go.Figure(data=[go.Pie(labels = cols, values = val)])
  return fig

def notes(df):
  res = df.langue.value_counts()
  return res

def notes1(df):
  data=pd.crosstab(df['langue']=='fr',df['Note'], normalize='index')
  fig=px.bar(data_frame=data, color='Note', range_x=('true', 'false'),
  title='Ventilation des notes chez les non-francophones (false) versus les francophones (true)')
  return fig


def photo_ou_non(df):
  cols = df['presence_photo'].unique()
  val = df['presence_photo'].value_counts()
  fig = go.Figure(data=[go.Pie(labels = cols, values = val)])
  return fig

def situation_famille(df):
  cols = df['Situation'].unique()
  val = df['Situation'].value_counts()
  fig = go.Figure(data=[go.Pie(labels = cols, values = val)])
  return fig

def par_pays(df):
  res = df.Pays.value_counts()
  return res

def nuage_de_mots(df,mask):
  data = df.commentaire
  wordCloud = wc.WordCloud(background_color="white", width=800, height=600, max_words=100, mask=mask).generate(str(data))
  plt.imshow(wordCloud, interpolation="bilinear")
  plt.axis('off')
  st.pyplot()



