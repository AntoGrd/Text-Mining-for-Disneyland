import streamlit as st
from fonctions_analyse import graph_sentiment,add_Sentiment

st.title('Analyse des sentiments')

Diagramme = st.sidebar.radio(
    "Selectionner sur quelles informations l'analyse des sentiments doit-elle être faite ?",
    ("Les titres", "Les commentaires"))

if Diagramme == "Les titres":
    col = 'sentiment_titre_commentaire'
elif Diagramme == "Les commentaires":
    col = 'sentiment_commentaire'

monument = ['Non','Oui']
selection = st.selectbox(f'Voulez-vous le graphique de sentiment pour une année précise',monument)
option = 'None'

if st.session_state['monument'] == 'Hotels':
    st.session_state['Hotels_sentiment'] = add_Sentiment(st.session_state['Hotels'])
    année = st.session_state['Hotels_sentiment'].Annee_avis.unique()
    if selection == 'Non':
        option = 'None'
    elif selection == 'Oui':
        option = st.selectbox('Selectionner l\' année que vous souhaitez', année)
    st.plotly_chart(graph_sentiment(st.session_state['Hotels_sentiment'],col, option))

elif st.session_state['monument']  == 'Parcs':  
    st.session_state['Parcs_sentiment'] = add_Sentiment(st.session_state['Parcs'])
    année = st.session_state['Parcs_sentiment'].Annee_avis.unique()
    if selection == 'Non':
        option = 'None'
    elif selection == 'Oui':
        option = st.selectbox('Selectionner l\' année que vous souhaitez', année)
    st.plotly_chart(graph_sentiment(st.session_state['Parcs_sentiment'],col, option))







