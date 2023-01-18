import streamlit as st
import plotly.express as px
from Analyse_de_base_hotels import nombre_avis_par_années,répartition_des_notes,notes,notes1,photo_ou_non,situation_famille,par_pays
import streamlit.components.v1 as components
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
import plotly.graph_objs as go
import chart_studio.plotly

st.subheader('Données du lieu choisi')

#################### PARCS ##############
if st.session_state['monument']  == 'Parcs':
    # Choix des différents graphiques
    Diagramme = st.sidebar.radio(
        "Quel diagramme voulez-vous afficher ?",
        ("Nombre d'avis par année", "Répartition des notes", 'Différence des notes entre les francophones et les étrangers','Répartition des commentaires avec ou sans photos',"Nombre d'avis par pays"))

    # Affichage des graphiques
    if Diagramme == "Nombre d'avis par année":
        st.plotly_chart(figure_or_data=nombre_avis_par_années(st.session_state['Parcs']),
                        use_container_width=True, sharing="streamlit", theme="streamlit")
           
        
    if Diagramme == "Répartition des notes":
        st.plotly_chart(figure_or_data=répartition_des_notes(st.session_state['Parcs']),
                        use_container_width=True, sharing="streamlit", theme="streamlit")
        
    if Diagramme == "Différence des notes entre les francophones et les étrangers":
        st.plotly_chart(figure_or_data=notes1(st.session_state['Parcs']),
                        use_container_width=True, sharing="streamlit", theme="streamlit")
            
      
    if Diagramme == "Répartition des commentaires avec ou sans photos":
        st.plotly_chart(figure_or_data=photo_ou_non(st.session_state['Parcs']),
                        use_container_width=True, sharing="streamlit", theme="streamlit")
        
    if Diagramme == "Nombre d'avis par pays":
        st.plotly_chart(figure_or_data=par_pays(st.session_state['Parcs']),
                        use_container_width=True, sharing="streamlit", theme="streamlit")

####################### Hotels ###################
if st.session_state['monument']  == 'Hotels':
    # Choix des différents graphiques
    Diagramme = st.sidebar.radio(
        "Quel diagramme voulez-vous afficher ?",
        ("Nombre d'avis par année", "Répartition des notes", 'Différence des notes entre les francophones et les étrangers','Répartition des commentaires avec ou sans photos',"Nombre d'avis par pays"))

    # Affichage des graphiques
    if Diagramme == "Nombre d'avis par année":
        st.plotly_chart(figure_or_data=nombre_avis_par_années(st.session_state['Hotels']),
                        use_container_width=True, sharing="streamlit", theme="streamlit")
           
        
    if Diagramme == "Répartition des notes":
        st.plotly_chart(figure_or_data=répartition_des_notes(st.session_state['Hotels']),
                        use_container_width=True, sharing="streamlit", theme="streamlit")
        
    if Diagramme == "Différence des notes entre les francophones et les étrangers":
        st.plotly_chart(figure_or_data=notes1(st.session_state['Hotels']),
                        use_container_width=True, sharing="streamlit", theme="streamlit")
            
      
    if Diagramme == "Répartition des commentaires avec ou sans photos":
        st.plotly_chart(figure_or_data=photo_ou_non(st.session_state['Hotels']),
                        use_container_width=True, sharing="streamlit", theme="streamlit")
        
    if Diagramme == "Nombre d'avis par pays":
        st.plotly_chart(figure_or_data=par_pays(st.session_state['Hotels']),
                        use_container_width=True, sharing="streamlit", theme="streamlit")