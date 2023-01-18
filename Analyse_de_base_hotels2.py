import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer

@st.cache
def nombre_avis_par_années(df):
  data = df.Annee_Avis.value_counts().reset_index()
  data.columns = ['Annee_Avis', 'Nombre']
  fig = px.bar(data_frame=data, x='Annee_Avis', y='Nombre',
                         labels={'Annee_Avis':'Année'}, title='Nombre de commentaires par année')
  return fig

@st.cache
def répartition_des_notes(df):
  data = df['Note'].value_counts()
  data.columns = ['Note', 'Nombre']
  cols = ['b','c','y','orange','r']
  names = [5,4,3,2,1]
  fig=px.pie(data_frame=data,values='Note', labels='note', names=names, color='Note',
             title='Répartition des notes attribuées')
  
  return fig

@st.cache
def notes(df):
  data=df['langue'].value_counts().reset_index()
  data.columns = ['langue', 'Nombre']
  fig=px.bar(data_frame=data,x="langue",y='Nombre', title='Nombre de commentaires')
  
  return fig

@st.cache
def notes1(df):
  data=pd.crosstab(df['langue']=='fr',df['Note'], normalize='index')
  cols = ['r','orange', 'y','c','b']
  names = ['Non francophones', 'Francophones']
  fig=px.bar(data_frame=data, color='Note', range_x=('true', 'false'),
                         title='Ventilation des notes chez les non-francophones (false) versus les francophones (true)')
  return fig

@st.cache
def photo_ou_non(df):
  data = df['Photo'].value_counts().reset_index()
  cols = ['b','c','y','orange','r']
  data.columns = ['Photo', 'Nombre']
  names = ['yes', 'no']
  fig=px.pie(data_frame=data,values='Photo', labels='Photo', names=names, color='Photo', 
             title='Répartition des notes attribuées')
  return fig

@st.cache
def situation_famille(df):
  cols = ['b','c','y','orange','r']
  val = df['Situation'].value_counts()
  val.plot.pie(autopct='%1.1f%%', shadow= True,colors=cols)
  st.pyplot
  st.set_option('deprecation.showPyplotGlobalUse', False)
  
@st.cache
def par_pays(df):
  data=df['Pays'].value_counts().reset_index()
  data.columns = ['Pays', 'Nombre']
  fig=px.bar(data_frame=data,x="Pays",y='Nombre',
             labels={'Pays':'Pays'}, title='Nombre de commentaires selon le pays')
  return fig


