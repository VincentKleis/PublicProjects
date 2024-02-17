from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
from json import load
import pickle
from sentimentalyse_funcs import balance

data_3class = {}
for name in ["train", "dev", "test"]:
    with open(f"setningsanalyse/norec_sentence/3class/{name}.json") as infile:
        data_3class[name] = load(infile)

text = {'train': [x['text'] for x in data_3class['train']], 
        'dev' : [x['text'] for x in data_3class['dev']],
        'test':[x['text'] for x in data_3class['test']]}

labels ={'train':[x['label'] for x in data_3class['train']],
         'dev' : [x['label'] for x in data_3class['dev']],
         'test':[x['label'] for x in data_3class['test']]}

x_train = text['train']+text['test']
y_train = labels['train']+labels['test']

nb_nlp = {'medium': spacy.load('nb_core_news_md')}


text_comb = text['train'] + text['test'] + text['dev']
labels_comb = labels['train'] + labels['test'] + labels['dev']

bal_text_comb,bal_label_comb = balance(text_comb, labels_comb, 1663)

pipe = Pipeline([('vect', TfidfVectorizer(ngram_range=(1,1), min_df=2, use_idf=True)),
                 ('clf', SVC(C=1000, gamma=1))])

pipe.fit(bal_text_comb, bal_label_comb)

model = "setningsanalyse/finalized_model.sav"
pickle.dump(pipe, open(model, 'wb'))