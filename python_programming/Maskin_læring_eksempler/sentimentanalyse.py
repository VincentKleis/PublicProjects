import pickle
from sklearn.pipeline import Pipeline
import spacy
from setningsanalyse.sentimentalyse_funcs import lemmatizer

nb_nlp = {'medium': spacy.load('nb_core_news_md')}

pipe = pickle.load(open("setningsanalyse/finalized_model.sav", 'rb'))

def pred_n_return(pipe:Pipeline, nlp:spacy, stop:bool, sentences:list=[]):
    """tries to predict the sentiment of a list of senteces if a list of sentences is given, 
    else it prompts for sentence until told to stop

    Args:
        pipe (Pipeline): a sklearn pipeline
        nlp (spacy): a language model
        stop (bool): if stopword removal should be implemented or not
        sentences (list): list of sentences that is empty by defaul
    """
    sent = ''
    if sentences==[]:
        while sent != ['stop']:
            sent = [input("Type 'stop' to stop \nType a sentence in norwegian:")]
            sent = lemmatizer(sent, nlp, stop)
            result = pipe.predict(sent)
            print(f"the sentence is {result[0]}")
    else:
        sent = lemmatizer(sentences, nlp, stop)
        result = pipe.predict(sent)
        for i in range(0, len(result)):
            print(sentences[i], 'is:', result[i])


# if empty wil prompt continusly for sentences
list_of_sent = []
pred_n_return(pipe, nb_nlp['medium'], True, list_of_sent)