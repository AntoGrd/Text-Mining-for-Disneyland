import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from gensim.models import Word2Vec
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from gensim.models import Word2Vec
import streamlit as st
import plotly.graph_objects as go
import os

parseur = CountVectorizer()

def mots_significatif_par_note2(df, nb_mots = 5):
    # Récupération du dataframe pour toutes les notes)
    X = parseur.fit_transform(df['com_cluster'])
    mdt = X.toarray()
    # On compte la fréquence de chaque mot dans notre DataFrame
    freq_mots = np.sum(mdt,axis=0)
    # Récupération des index des mots qui reviennent le plus (ordre décroissant)
    index = np.argsort(freq_mots)
    imp = {'terme': np.asarray(parseur.get_feature_names_out())[index], 'freq':freq_mots[index]}
    imp1 = pd.DataFrame.from_dict(imp, orient='columns')
    imp2 = imp1.sort_values(by = 'freq', ascending = False)
    # Affichage des 5 mots qui ressortent le plus (ou un autre nombre si l'on a mis autre chose que 5)
    import matplotlib.pyplot as plt
    poids = imp2['freq'].head(nb_mots)
    bars = imp2['terme'].head(nb_mots)
    fig = go.Figure(data=[go.Bar(x = bars, y = poids)])
    return fig


def x_mots_plus_courants(df, nb_mots = 5):
    X = parseur.fit_transform(df['com_cluster'])
    mdt = X.toarray()
    # On compte la fréquence de chaque mot dans notre DataFrame
    freq_mots = np.sum(mdt,axis=0)
    # Récupération des index des mots qui reviennent le plus (ordre décroissant)
    index = np.argsort(freq_mots)
    imp = {'terme': np.asarray(parseur.get_feature_names_out())[index], 'freq':freq_mots[index]}
    imp1 = pd.DataFrame.from_dict(imp, orient='columns')
    imp2 = imp1.sort_values(by = 'freq', ascending = False)
    top_des_mots = (imp2['terme'].head(nb_mots))
    return (top_des_mots)

