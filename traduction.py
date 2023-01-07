from googletrans import Translator, constants
from langdetect import detect

def translate(df):
    translator = Translator()
    commentaires=df["comm"]
    titres=df["titre_comm"]
    langue=[]
    commentaires_fr=[]
    titres_fr=[]
    for c in range(len(commentaires)):
        l=detect(commentaires[c])
        langue.append(l)
        if l=='fr':
            commentaires_fr.append(commentaires[c])
            titres_fr.append(titres[c])
        else:
            traduction=translator.translate(commentaires[c],src=l, dest="fr")
            commentaires_fr.append(traduction.text)
            
            traduction=translator.translate(titres[c],src=l, dest="fr")
            titres_fr.append(traduction.text)
            
    df["comm"]=commentaires_fr
    df["titre_comm"]=titres_fr
    df.insert(5,"langue",langue)
    