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

parseur = CountVectorizer()
ParcDisney = (pd.read_csv("C:/Users/laura/Downloads/Text-Mining-for-Disneyland-main (1)/Text-Mining-for-Disneyland-main/data_clean/Disneyland_Paris_clean.csv", sep=","))
    

# Fonction qui donne les 5 (par défault) mots les plus cités dans le dataframe (df) pour toutes les notes (par défault) 
def mots_significatif_par_note(df, variable = 'toutes', modalité = 'toutes',  nb_mots = 5):
    # Récupération du dataframe pour toutes les notes
    a = df.columns
    dfnew = pd.DataFrame(columns=a)
    # Si base complète on prend tout notre dataframe
    if (variable == 'toutes') :
        if (modalité == 'toutes'):
            dfnew = df
    # Si on ne choisit que quelques variables 
    else :
        # Si on prend toutes les modalités on prend tout notre dataFrame
        for i in range (0,len(variable)) : 
            if (modalité[i] == 'toutes'):
                dfnew = df
            else :
                # Sinon on récupère uniquement les lignes que l'on souhaite
                for j in range (0,len(modalité[i])):
                    # On récupère l'ensemble des modalités de notre variable
                    dfnew = dfnew.append(df[df[variable[i]]==modalité[i][j]])
    parseur = CountVectorizer()
    X = parseur.fit_transform(dfnew['commentaire'])
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
    y_pos = np.arange(len(bars))
    plt.bar(y_pos,poids)

def mots_significatif_par_note2(df, nb_mots = 5):
    # Récupération du dataframe pour toutes les notes)
    X = parseur.fit_transform(df['commentaire'])
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
    X = parseur.fit_transform(df['commentaire'])
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

#######################################################################################

#Transformer les chaînes de caractères de liste en liste 
import ast
from collections import Iterable
from nltk.probability import FreqDist
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

#Transform list 
def flatten(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:        
             yield item

# Initialisation de SentimentIntensityAnalyzer.
#ajout des sentiments 
def ScoreSentiment(vector):
    tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
     
    senti_list = []
    for i in vector.commentaires:
        vs = tb(i).sentiment[0]
        if (vs > 0):
            senti_list.append('Positive')
        elif (vs < 0):
            senti_list.append('Negative')
        else:
            senti_list.append('Neutral') 
            
    return senti_list


#frequence de mots + ajout de la variable sentiment selon le titre du commentaire
#sentiment : define between commentaire / titre_commentaire
def freqMot(df,sentiment, tailleliste): 
    
     tailleliste = int(tailleliste)
     liste = ["commentaire", "titre_commentaire"]
     liste_comm = []
     liste_titre_com = []
     for item in liste :
         
         commentaire = [ast.literal_eval(x) for x in df[item].tolist()]
         commentaire_transform = list(flatten(commentaire))

         fdist = FreqDist(commentaire_transform)

         if item == "commentaire":
            liste_comm.append(fdist.most_common(tailleliste))
            
            if sentiment == "commentaire":
                documents =[" ".join(doc) for doc in commentaire]
                parc_com = pd.DataFrame({'commentaires': documents})
                df['sentiment'] = ScoreSentiment(parc_com)
                 
         else :
             liste_titre_com.append(fdist.most_common(tailleliste))
             
             if sentiment == "titre_commentaire":
                 documents =[" ".join(doc) for doc in commentaire]
                 parc_com = pd.DataFrame({'commentaires': documents})
                 df['sentiment'] = ScoreSentiment(parc_com)
                 
        
     dfreq = pd.DataFrame(zip(liste_comm,liste_titre_com))
     dfreq.columns = ["commentaire", "titre_commentaire"]
     

     return df, dfreq
 
d_sentiment = freqMot(parcDisney, "titre_commentaire", 10)[0]

d_freq = freqMot(parcDisney, "titre_commentaire", 10)[1]

d_freq["commentaire"].str.split(",")


d_sentiment["sentiment"].value_counts()


from wordcloud import WordCloud
import matplotlib.pyplot as plt

commentaire = [ast.literal_eval(x) for x in d_sentiment.commentaire.tolist()]

documents =[" ".join(doc) for doc in commentaire]
parc_com = pd.DataFrame({'commentaires': documents})

allWords = ' '.join([twts for twts in parc_com.commentaires])
wordCloud = WordCloud(width=500, height=300, random_state=5000, max_font_size=110).generate(allWords)

plt.imshow(wordCloud, interpolation="bilinear")
plt.axis('off')

plt.show()


import plotly.express as px
"""
#sentiment 
fig = px.histogram(d, x="sentiment",color="sentiment")
fig.update_layout(
    title_text='Sentiment of reviews', # title of plot
    xaxis_title_text='Sentiment', # xaxis label
    yaxis_title_text='Count', # yaxis label
    bargap=0.2, 
    bargroupgap=0.1
)
fig.show()

#sentiment par année
fig = px.histogram(d, x="Annee_Sejour",color="sentiment")
fig.update_layout(
    title_text='Sentiments per Year', # title of plot
    xaxis_title_text='Year', # xaxis label
    yaxis_title_text='Number of Comments', # yaxis label
    bargap=0.2, 
    bargroupgap=0.1
)
fig.show()

#sentiment par mois
fig = px.histogram(d, x="Mois_Sejour",color="sentiment")
fig.update_layout(
    title_text='Sentiments per Month', # title of plot
    xaxis_title_text='Month', # xaxis label
    yaxis_title_text='Number of Comments', # yaxis label
    bargap=0.2, 
    bargroupgap=0.1
)
fig.show()
"""

#select annee
def graph_sentiment(df , col, annee = "None"):
    
    if annee =="None":
        fig = px.histogram(df, x=col,color="sentiment")
        
    else:
        d_annee = df[(df['Annee_Sejour'] == annee) ].reset_index(drop=True)
        fig = px.histogram(d_annee, x=col,color="sentiment")
        
    fig.update_layout(
        title_text='Sentiment of reviews', # title of plot
        xaxis_title_text='Sentiment', # xaxis label
        yaxis_title_text='Count', # yaxis label
        bargap=0.2, 
        bargroupgap=0.1
    )
    
    
    return fig
 
        


#########################################################################################

from gensim.models import keyedvectors
from sklearn import preprocessing
os.chdir("C:/Users/Sam/Downloads/archive")

trained = keyedvectors.load_word2vec_format("GoogleNews-vectors-negative300.bin",binary=True,unicode_errors='ignore')

commentaire = [ast.literal_eval(x) for x in d_sentiment["titre_commentaire"].tolist()]

#librairie numpy
import numpy
from matplotlib import pyplot as plt


#fonction pour transformer un document en vecteur
#à partir des tokens qui le composent
#entrée : doc à traiter
#         modèle préentrainé
#sortie : vecteur représentant le document
def my_doc_2_vec(doc,trained):
    #dimension de représentation
    p = trained.vectors.shape[1]
    #initialiser le vecteur
    vec = numpy.zeros(p)
    #nombre de tokens trouvés
    nb = 0
    #traitement de chaque token du document
    for tk in doc:
        #ne traiter que les tokens reconnus
        try:
            values = trained[tk]
            vec = vec + values
            nb = nb + 1.0
        except:
            pass
    #faire la moyenne des valeurs
    #uniquement si on a trové des tokens reconnus bien sûr
    if (nb > 0.0):
        vec = vec/nb
    #renvoyer le vecteur
    #si aucun token trouvé, on a un vecteur de valeurs nulles
    return vec


#traiter les documents du corpus corpus
docsVec = list()
#pour chaque document du corpus nettoyé
for doc in commentaire:
    #calcul de son vecteur
    vec = my_doc_2_vec(doc,trained)
    #ajouter dans la liste
    docsVec.append(vec)
#transformer en matrice numpy
matVec = numpy.array(docsVec)
print(matVec.shape)


Transposed_Dataset = pd.DataFrame(matVec).T

X_scaled = preprocessing.scale(Transposed_Dataset)


X_std = preprocessing.StandardScaler().fit_transform(X_scaled)

from sklearn.decomposition import PCA

sklearn_pca = PCA(n_components = 4) # Using PCA to remove cols which has less co-relation
Y_sklearn = sklearn_pca.fit_transform(matVec) #fit_transform() is used to scale training data to learn parameters such as 
# mean & variance of the features of training set and then these parameters are used to scale our testing data.
# As concluded using Elbow Method.
df = px.data.iris()
df['species']
fig = px.scatter(Y_sklearn, x=0, y=1, color=d_sentiment["sentiment"])

from plotly.offline import plot
plot(fig)  #voir le graph

#fig.show()

def elbow_method(Y_sklearn):
    """
    This is the function used to get optimal number of clusters in order to feed to the k-means clustering algorithm.
    """

    number_clusters = range(1, 7)  # Range of possible clusters that can be generated
    kmeans = [KMeans(n_clusters=i, max_iter = 600) for i in number_clusters] # Getting no. of clusters 

    score = [kmeans[i].fit(Y_sklearn).score(Y_sklearn) for i in range(len(kmeans))] # Getting score corresponding to each cluster.
    score = [i*-1 for i in score] # Getting list of positive scores.
    
    plt.plot(number_clusters, score)
    plt.xlabel('Number of Clusters')
    plt.ylabel('Score')
    plt.title('Elbow Method')
    plt.show()
elbow_method(Y_sklearn)
# Optimal Clusters = 2



from sklearn.cluster import KMeans
n_clusters = 3
kmeans = KMeans(n_clusters= n_clusters, max_iter=400, algorithm = 'auto')# Partition 'n' no. of observations into 'k' no. of clusters. 
fitted = kmeans.fit(Y_sklearn) # Fitting k-means model  to feature array
prediction = kmeans.predict(Y_sklearn) # predicting clusters class '0' or '1' corresponding to 'n' no. of observations


def kmeans_clustering(Y_sklearn, fitted):
    """
    This function will predict clusters on training set and plot the visuals of clusters as well.
    """

    plt.scatter(Y_sklearn[:, 0], Y_sklearn[:, 1],c=prediction ,s=50, cmap='viridis') # Plotting scatter plot 
    centers2 = fitted.cluster_centers_ # It will give best possible coordinates of cluster center after fitting k-means
    plt.scatter(centers2[:, 0], centers2[:, 1],c='black', s=300, alpha=0.6);
    # As this can be seen from the figure, there is an outlier as well.
    
kmeans_clustering(Y_sklearn, fitted)







"""

#creation modele 

from gensim.models import Word2Vec
modele = Word2Vec(commentaire,window=4) #size = 2 ; 2 axes #window= 5 termes-voisins

words= modele.wv

############# test avec variable cible sentiment
#transformer en data frame
df = pd.DataFrame(words.vectors,columns=["v"+str(i+1) for i in range(words.vectors.shape[1])])
df['Note'] = parcDisney["Note"]
df.head()

from sklearn.model_selection import train_test_split
dfTrain, dfTest = train_test_split(df,train_size=0.7,stratify=df['Note'] , random_state=0)

#from imblearn.under_sampling import ClusterCentroids
#cc = ClusterCentroids()
#X_res, y_res = cc.fit_resample(dfTrain[dfTrain.columns[:-1]],dfTrain['sentiment'])


#SVM avec un noyau RBF par défaut
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(dfTrain[dfTrain.columns[:-1]],dfTrain['sentiment'])

#prédiction en tests
pred = clf.predict(dfTest[dfTest.columns[:-1]])
print(pred.shape)

#évaluation des performances
from sklearn import metrics
print(metrics.classification_report(dfTest.sentiment,pred))

from sklearn.metrics import confusion_matrix
confusion_matrix(dfTest.sentiment,pred)
 

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score
from sklearn.neural_network import MLPClassifier

names=[]
f1score_ =[]

models={'SVC': SVC(),
       'RandomForest': RandomForestClassifier(),
       'DecisionTree': DecisionTreeClassifier(),
       'Naïve Bayes': GaussianNB(), 
       'Neural Network': MLPClassifier()}

for name, model in models.items():
    name_model = model
    name_fit = name_model.fit(dfTrain[dfTrain.columns[:-1]],dfTrain['Note'])
    name_pred = name_fit.predict(dfTest[dfTest.columns[:-1]])
    f1score = f1_score(dfTest.Note,name_pred, average = "micro")
    names.append(name)
    f1score_.append(f1score)

score_df = pd.DataFrame(zip(names, f1score_))
score_df.columns = ["Nom", "Score"]

index = score_df.Score.idxmax()

name_model = list(models.values())[index]
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
crossvalidation=KFold(n_splits=5,shuffle=True,random_state=1)
search_grid={'C':[1,10,100,500],'gamma':[1,0.1,0.001], 'kernel':['linear','rbf']}
search=GridSearchCV(estimator=name_model,param_grid=search_grid,scoring='f1_weighted',n_jobs=1,cv=crossvalidation)
search.fit(dfTrain[dfTrain.columns[:-1]],dfTrain['sentiment'])

search.best_params_

##############test variable cible note 

os.chdir("C:/Users/Sam/Downloads/archive")

from gensim.models import keyedvectors
trained = keyedvectors.load_word2vec_format("GoogleNews-vectors-negative300.bin",binary=True,unicode_errors='ignore')

commentaire = [ast.literal_eval(x) for x in parcDisney["titre_commentaire"].tolist()]


#librairie numpy
import numpy

#fonction pour transformer un document en vecteur
#à partir des tokens qui le composent
#entrée : doc à traiter
#         modèle préentrainé
#sortie : vecteur représentant le document
def my_doc_2_vec(doc,trained):
    #dimension de représentation
    p = trained.vectors.shape[1]
    #initialiser le vecteur
    vec = numpy.zeros(p)
    #nombre de tokens trouvés
    nb = 0
    #traitement de chaque token du document
    for tk in doc:
        #ne traiter que les tokens reconnus
        try:
            values = trained[tk]
            vec = vec + values
            nb = nb + 1.0
        except:
            pass
    #faire la moyenne des valeurs
    #uniquement si on a trové des tokens reconnus bien sûr
    if (nb > 0.0):
        vec = vec/nb
    #renvoyer le vecteur
    #si aucun token trouvé, on a un vecteur de valeurs nulles
    return vec




#traiter les documents du corpus corpus
docsVec = list()
#pour chaque document du corpus nettoyé
for doc in commentaire:
    #calcul de son vecteur
    vec = my_doc_2_vec(doc,trained)
    #ajouter dans la liste
    docsVec.append(vec)
#transformer en matrice numpy
matVec = numpy.array(docsVec)
print(matVec.shape)


#transformer en data frame
#df = pd.DataFrame(matVec,columns=["v"+str(i+1) for i in range(matVec.shape[1])])
#df['Note'] = parcDisney["Note"]
#df.head()



df = pd.DataFrame(matVec,columns=["v"+str(i+1) for i in range(matVec.shape[1])])
df['Note'] = parcDisney["Note"]
df.head()

from sklearn.model_selection import train_test_split
dfTrain, dfTest = train_test_split(df, train_size=0.7, random_state=0)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

names=[]
f1score_ =[]

models={'SVC': SVC(),
       'RandomForest': RandomForestClassifier(),
       'DecisionTree': DecisionTreeClassifier(),
       'Naïve Bayes': GaussianNB(), 
       'Neural Network': MLPClassifier(),
       'knn' : KNeighborsClassifier()}

#X = parcDisney.drop(["Note"], axis = 1)

for name, model in models.items():
    name_model = model
    name_fit = name_model.fit(dfTrain[dfTrain.columns[:-1]],dfTrain['Note'])
    name_pred = name_fit.predict(dfTest[dfTest.columns[:-1]])
    f1score = f1_score(dfTest.Note,name_pred, average = "macro")
    names.append(name)
    f1score_.append(f1score)

score_df = pd.DataFrame(zip(names, f1score_))
score_df.columns = ["Nom", "Score"]

index = score_df.Score.idxmax()

name_model = list(models.values())[index]




from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
crossvalidation=KFold(n_splits=2,shuffle=True,random_state=1)

param_grid = { 
    'n_estimators': [200, 500, 1000, 2000, 2500],
    'max_features': ['auto', 'sqrt', 'log2'],
    'max_depth' : [5,10,15, 20],
    'criterion' :['gini', 'entropy']
}

search1=GridSearchCV(estimator=RandomForestClassifier(),param_grid=param_grid,n_jobs=1,cv=2)
search1.fit(dfTrain[dfTrain.columns[:-1]],dfTrain['Note'])

par1 = search1.best_params_



from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
crossvalidation=KFold(n_splits=2,shuffle=True,random_state=1)

search_grid={'C':[1,10,100,500],'gamma':[1,0.1,0.001], 'kernel':['linear','rbf']}

search2=GridSearchCV(estimator=SVC(),param_grid=search_grid,n_jobs=1,cv=2)
search2.fit(dfTrain[dfTrain.columns[:-1]],dfTrain['Note'])







from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
crossvalidation=KFold(n_splits=2,shuffle=True,random_state=1)

parameter_space = {
    'hidden_layer_sizes': [(50,50,50), (50,100,50), (100,)],
    'max_iter': [1000,1100,1200,1500,1600,1700,1900,2000 ],
    'activation': ['tanh', 'relu'],
    'solver': ['sgd', 'adam'],
    'alpha': [0.0001, 0.05],
    'learning_rate': ['constant','adaptive'],
}

search=GridSearchCV(estimator=name_model,param_grid=parameter_space,n_jobs=1,cv=2)
search.fit(dfTrain[dfTrain.columns[:-1]],dfTrain['Note'])

"""
{'activation': 'relu',
 'alpha': 0.0001,
 'hidden_layer_sizes': (50, 50, 50),
 'learning_rate': 'constant',
 'max_iter': 1200,
 'solver': 'sgd'}
"""

param= search.best_params_

modele = search.best_estimator_.fit(dfTrain[dfTrain.columns[:-1]],dfTrain['Note'])
pred = modele.predict(dfTest[dfTest.columns[:-1]])

f1score = f1_score(dfTest.Note,pred, average = "weighted")


modele = MLPClassifier(**search.best_params_).fit(dfTrain[dfTrain.columns[:-1]],dfTrain['Note'])
pred = modele.predict(dfTest[dfTest.columns[:-1]])
f1score = f1_score(dfTest.Note,pred, average = "weighted")!






######################################################Test 3 ################################## 

from sklearn.feature_extraction.text import CountVectorizer


commentaire = [ast.literal_eval(x) for x in parcDisney["titre_commentaire"].tolist()]

com_ = [' '.join(w) for w in commentaire]

df = pd.DataFrame.from_dict({'Note':parcDisney["Note"],'Com':pd.Series(com_)})



from sklearn.model_selection import train_test_split
dfTrain, dfTest = train_test_split(df, train_size=0.7,stratify= df['Note'],random_state=0)

init = CountVectorizer()

XTrain = init.fit_transform(dfTrain.Com).toarray()

XTest = init.transform(dfTest.Com).toarray()



from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

names=[]
f1score_ =[]

models={'SVC': SVC(),
       'RandomForest': RandomForestClassifier(),
       'DecisionTree': DecisionTreeClassifier(),
       'Naïve Bayes': GaussianNB(), 
       'Neural Network': MLPClassifier(),
       'knn' : KNeighborsClassifier()}

#X = parcDisney.drop(["Note"], axis = 1)

for name, model in models.items():
    name_model = model
    name_fit = name_model.fit(XTrain,dfTrain['Note'])
    name_pred = name_fit.predict(XTest)
    f1score = f1_score(dfTest['Note'],name_pred, average = "macro")
    names.append(name)
    f1score_.append(f1score)

score_df = pd.DataFrame(zip(names, f1score_))
score_df.columns = ["Nom", "Score"]


"""
