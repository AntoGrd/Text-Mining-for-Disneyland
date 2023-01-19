import streamlit as st
from fonctions_analyse import graph_sentiment,add_Sentiment
from Text_clustering import get_top_keywords

st.title('hgv')

Diagramme = st.sidebar.radio(
    "Selectionner sur quelles informations l'analyse des sentiments doit-elle être faite ?",
    ("Les titres", "Les commentaires"))

if Diagramme == "Les titres":
    col = 'sentiment_titre_commentaire'
elif Diagramme == "Les commentaires":
    col = 'sentiment_commentaire'
if st.session_state['monument'] == 'Hotels':
    data = st.session_state['Hotels']
elif st.session_state['monument']  == 'Parcs':
    data = st.session_state['Parcs']
st.plotly_chart(graph_sentiment(add_Sentiment(data),col))
