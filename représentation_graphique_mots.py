# IMPORTATION
# /!\ Il faut récupérer la fonction GetAnalysis 
# On peut aussi par la suite appler des fonction du fichier Similarité_de_mots.py pour plus d'infos 
import wordcloud
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
import ast
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from statsmodels.stats.anova import anova2_lm_single
from gensim.models import Word2Vec
from wordcloud import WordCloud

# Fonction qui donnent la répartition des sentiments + histogramme + nuage de mots
def analyse_sentiments (df, repartition_sentiments1 = 'oui', repartition_sentiments2 = 'oui', histogramme_sentiments = 'oui', nuage_de_mots = 'oui'):
  liste = [ast.literal_eval(x) for x in df.commentaire]
  data =[" ".join(doc) for doc in liste]
  data = pd.DataFrame({'commentaires': data})
  nltk.download('vader_lexicon')
  vader = SentimentIntensityAnalyzer()
  function = lambda title: vader.polarity_scores(title)['compound']
  data['score'] = data['commentaires'].apply(function)
  data['sentiment'] = data['score'].apply(getAnalysis)
  if repartition_sentiments1 == 'oui':
    plt.title('Analyse des sentiments')
    plt.xlabel('Sentiment')
    plt.ylabel('nombre de commentaires')
    data['sentiment'].value_counts().plot(kind = 'bar')
    plt.show()
  if repartition_sentiments2 == 'oui':
    data.sentiment.value_counts().plot(kind='pie', autopct='%1.0f%%',  fontsize=12, figsize=(9,6), colors=["blue", "yellow","red"])
    plt.ylabel("Répartition des sentiments des commentaires", size=14)
  if histogramme_sentiments == 'oui':
    plt.figure(figsize=(8, 5))
    sns.histplot(data, x='score', color="darkblue", bins=10, binrange=(-1, 1))
    plt.title("Ventilation des sentiments exprimés dans les commentaires")
    plt.xlabel("Compound Scores")
    plt.ylabel("")
    plt.tight_layout()
  if nuage_de_mots == 'oui':
    allWords = ' '.join([twts for twts in data['commentaires']])
    wordCloud = WordCloud(width=500, height=300, random_state=5000, max_font_size=110).generate(allWords)
    plt.figure(figsize=(8, 8))
    plt.imshow(wordCloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()

analyse_sentiments(parcDisney)

# Fonction qui donne la représenation vectorielle des x mots les plus présents (par défault)
def representation_mots(df, nb_mots = 10):
  liste = [ast.literal_eval(x) for x in parcDisney.commentaire]
  modele = Word2Vec(liste,vector_size=2,window=5)
  words = modele.wv
  data = pd.DataFrame(words.vectors, columns=['V1','V2'], index=words.key_to_index.keys())
  mots2 = words.key_to_index.keys()
  mots2 = list(mots2)[0:nb_mots]
  dataMots2= data.loc[mots2]
  plt.figure(figsize=(15, 15))
  for i in range(dataMots2.shape[0]):
     plt.scatter(dataMots2.V1,dataMots2.V2,s=30)
     plt.annotate(dataMots2.index[i],(dataMots2.V1[i],dataMots2.V2[i]))
  plt.show()
  
  representation_mots(parcDisney)
