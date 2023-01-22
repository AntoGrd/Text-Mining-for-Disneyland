import streamlit as st
from Text_clustering import text_clustering


st.title('Analyse de texte')

nb_cluster = st.sidebar.slider('Combien de cluster souhaitez-vous? ', 0, 20, 3)
nb_mots = st.sidebar.slider('Combien de mots par cluster souhaitez-vous? ', 0 , 50, 10)


choix_cluster = ["Choix de l'analyse","Titre des commentaires", "Commentaires"]
selection_cluster = st.selectbox(f'Choisissez si vous voulez créer des clusters sur les titres ou sur les commentaires',choix_cluster)
st.session_state['choix_cluster'] = selection_cluster

if selection_cluster == 'Titre des commentaires':
    if st.session_state['monument'] == 'Parcs':
        retour = text_clustering(st.session_state['Parcs'],'com_titre_cluster',nb_cluster,nb_mots)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.write(retour[0])
        st.write(retour[1])
        st.pyplot(retour[2])
    if st.session_state['monument'] == 'Hotels':
        retour = text_clustering(st.session_state['Hotels'],'com_titre_cluster',nb_cluster,nb_mots)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.write(retour[0])
        st.write(retour[1])
        st.pyplot(retour[2])
        
if selection_cluster == 'Commentaires':
    if st.session_state['monument'] == 'Parcs':
        retour = text_clustering(st.session_state['Parcs'],'com_cluster',nb_cluster,nb_mots)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.write(retour[0])
        st.write(retour[1])
        st.pyplot(retour[2])
    if st.session_state['monument'] == 'Hotels':
        retour = text_clustering(st.session_state['Hotels'],'com_cluster',nb_cluster,nb_mots)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.write(retour[0])
        st.write(retour[1])
        st.pyplot(retour[2])
