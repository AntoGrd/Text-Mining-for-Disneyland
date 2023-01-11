import streamlit as st
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import numpy as np
import shap
import matplotlib.pyplot as plt

def train_and_explain_model(corpus, y, years, months, test_size=0.2, random_state=7):
    shap.initjs()

    year = st.slider("Select year", int(min(years)), int(max(years)))

    corpus_year = corpus[years==Annee_avis]

    y_year = y[years==Annee_avis]

    month = st.selectbox("Sélectionnez une année", range(1, 13))
    corpus_month = corpus[months==Mois_avis]
    y_month = y[months==Mois_avis]

    corpus_train, corpus_test, y_train, y_test = train_test_split(corpus_month, y_month, test_size=test_size, random_state=random_state)
    vectorizer = TfidfVectorizer(min_df=10)
    X_train = vectorizer.fit_transform(corpus_train)
    X_test = vectorizer.transform(corpus_test)
    model = sklearn.linear_model.LogisticRegression(penalty="l2", C=0.1)
    model.fit(X_train, y_train)
    explainer = shap.LinearExplainer(model, X_train, feature_perturbation="interventional")
    shap_values = explainer.shap_values(X_test)
    X_test_array = X_test.toarray()

    st.subheader("Termes les plus impactant de la satisfaction-clients")

    st.write("Graphique récapitulatif - moyenne de l'importance des caractéristiques par classe.Axe des x :moyenne en valeur absolue. Couleur :valeur du terme dans le verbatim")
  
    st.pyplot()
    shap.summary_plot(shap_values, X_test_array, feature_names=vectorizer.get_feature_names_out())

    #class0=négatif, class1=positif, class2=neutre

    plt.legend(title='Sentiment', labels=['Négatif', 'Positif','Neutre')
    
    st.subheader("Diagramme interactif")
    st.write("Contribution de chaque terme/vecteur à la prédiction sur l'échantillon-test. Les vecteurs sont triés par similarité en fonction de l'ampleur de leur contribution"
)
   #sentiment négatif =0, sentiment positif=1
 ind = st.selectbox('Select index', range(X_test.shape[0]))
    shap.force_plot(explainer.expected_value[ind],shap_values[ind],feature_names=vectorizer.get_feature_names_out())
    plt.legend(title='Sentiment', labels=['Negatif', 'Positif'])
