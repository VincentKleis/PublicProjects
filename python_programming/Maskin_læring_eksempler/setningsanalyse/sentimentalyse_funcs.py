import spacy
from sklearn.pipeline import Pipeline

def lemmatizer(list_sentc:list, nlp:spacy, include_stop:bool)->list:
    """takes a list of sentences and returns a list of lemmatized sentences using the lemma_ 
    atribute from spacy, and list comprehention to filter out stopwords

    Args:
        list_sentc (list): a list of multiword sentences
        nlp (spacy): a spacy language model for lemmatization
        include_stop (bool): if true includes stopwords, if false removes stopwords
        
    Returns:
        list: lemmatized sentences
    """
    result = []
    for sentence in list_sentc:
        if nlp != None:
            doc = nlp(sentence.lower())
            if include_stop == False:
                result.append(' '.join([token.lemma_ for token in doc if token.is_stop is False]))
            else:
                result.append(' '.join([token.lemma_ for token in doc]))
        else:
            nlp = spacy.load('nb_core_news_sm')
            doc = nlp(sentence.lower())
            if include_stop == False:
                result.append(' '.join([token.text for token in doc if token.is_stop is False]))
            else:
                result.append(sentence)

    return result

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

def balance(text:list, labels:list, bal_len:int)->tuple:
    """balances input text based on labels, text and labels must correspond such that text[0] has label[0]

    Args:
        text (list): list of sentences
        labels (list): list of labels
        bal_len (int): what lenght the balanced text and labels should have

    Returns:
        tuple: resulting text and labels
    """
    result_text = []
    result_labels = []

    n_positive = 0
    n_neutral = 0
    n_negative = 0

    # balance by looking for labels, 
    # adding corresponding text and labels to a list 
    # and count different types of labels

    for index in range(0, len(labels)):
        label = labels[index]
        match label:
            case 'Positive':
                if n_positive < bal_len:
                    result_text.append(text[index])
                    result_labels.append(labels[index])
                    n_positive += 1
            
            case 'Neutral':
                if n_neutral < bal_len:
                    result_text.append(text[index])
                    result_labels.append(labels[index])
                    n_neutral += 1
            
            case 'Negative':
                if n_negative < bal_len:
                    result_text.append(text[index])
                    result_labels.append(labels[index])
                    n_negative += 1
    return result_text,result_labels