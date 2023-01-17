import os
import pandas as pd
import gensim
from gensim.models import CoherenceModel
from gensim.corpora import Dictionary
import pyLDAvis.gensim_models
import streamlit as st

#en entrée : 
    
#commentaires : la colonne des commentaires d'un hotel/parcs
#ntopics : le nombre de topics que l'on veut créer
#npasses : nombre de passages sur le data set pour établir le topic model
# plus il y a de passages, meilleur est le score de cohérence (à partir de 10000 passages on est
#censés avoir un score très proche de 70% donc assez satisfaisant mais très long, peut être tester avec
# ~100 dans un premier temps)

def lda(commentaires,ntopics, npasses):
    tokens = commentaires.apply(lambda x: x.replace("[","").replace("]","").replace("'","").split(","))
    tokens = tokens.apply(lambda x: [word.strip() for word in x])

    dictionary = Dictionary(tokens.tolist())
    dictionary.filter_extremes(no_below=15, no_above=0.1, keep_n=1000)
    bow_corpus = [dictionary.doc2bow(doc) for doc in tokens]
    lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics = ntopics, id2word = dictionary, passes = npasses)
    
    topics = []
    for idx, topic in lda_model.print_topics(-1) :
        topics.append(topic)
    #calcul de la cohérence du modèle
    coherence_model_lda = CoherenceModel(model=lda_model, texts=tokens, dictionary=dictionary)
    coherence_lda = coherence_model_lda.get_coherence()

    all_topic_model = []
    for i in range(len(topics)):
        str = topics[i].split(' + ')
        topic_model = []
        for j in range(10):
            weight = str[j][0:5]
            word = str[j][7:len(str[j])-1]
            topic_model.append((weight, word))
        all_topic_model.append(topic_model)
        
    df_topic_model = pd.DataFrame(all_topic_model)
    
    vis_data = pyLDAvis.gensim_models.prepare(lda_model, bow_corpus, dictionary) 
    pyLDAvis.display(vis_data)
    st.write(pyLDAvis.show(vis_data)) #si marche pas, essayer : st.pydeck_chart(vis_data.to_dict())

#exemple :
#os.chdir(r'C:\Documents\travail\LYON2\M2\text_mining\projet_disney\projet_disney\data_clean')
#tab=pd.read_csv('hotel_newport_clean.csv')
#lda(tab["commentaire"],5,100)