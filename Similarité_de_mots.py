import streamlit as st
import pandas as pd
import numpy as np
import ast
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def most_similar_mots(df, mot):
    liste = [ast.literal_eval(x) for x in df.commentaire]
    modele = Word2Vec(liste, vector_size=2, window=5)
    words = modele.wv
    if mot in words:
        similaires = words.most_similar(mot)
        st.write(f"Mots similaires à '{mot}':")
        st.write(similaires)
    else:
        st.write(f"Le mot '{mot}' n'est pas présent dans le vocabulaire du modèle.")
        
def most_similarity_mots(df, mot1, mot2):
    liste = [ast.literal_eval(x) for x in df.commentaire]
    modele = Word2Vec(liste, vector_size=2, window=5)
    words = modele.wv
    sim = words.similarity(mot1, mot2)
    st.write(f"Similarité entre {mot1} et {mot2} : {sim}")

def representation_mots2(df, liste_mots):
    liste = [ast.literal_eval(x) for x in df.commentaire]
    modele = Word2Vec(liste, vector_size=2, window=5)
    words = modele.wv
    df = pd.DataFrame(words.vectors, columns=["V1","V2"], index = words.key_to_index.keys())
    dfMots = df.loc[liste_mots,:]
    fig = go.Figure(data=[go.Scatter(x=dfMots.V1, y=dfMots.V2, mode='markers', text=dfMots.index, name="")])
    fig.update_layout(title={"text": "Répresentation des mots"})
    for i in range (dfMots.shape[0]):
        fig.add_trace(go.Scatter(x=[dfMots.V1[i]], y=[dfMots.V2[i]], name=dfMots.index[i], mode='text', text=[dfMots.index[i]]))
    st.plotly_chart(fig)
