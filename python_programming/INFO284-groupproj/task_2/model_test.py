
import spacy
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix

data_3class = {}
for name in ["train", "dev", "test"]:
    with open(f"norec_sentence/3class/{name}.json") as infile:
        data_3class[name] = json.load(infile)


# The data from thre json files named train, dev, and test are loaded are collected in the two dictionaries data_3class and data_binary

# Dataset cloned from github: https://github.com/ltgoslo/norec_sentence
# 
# Kutuzov, A., Barnes, J., Velldal, E., Øvrelid, L., & Oepen, S. (2021). Large-Scale Contextualised Language Modelling for Norwegian. Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa 2021).
# 
# Øvrelid, L., Mæhlum, P., Barnes, J., & Velldal, E. (2020). A Fine-grained Sentiment Dataset for Norwegian. Proceedings of the 12th Edition of the Language Resources and Evaluation Conference. Marseille, France, 2020.

# re structuring so that it is easier to work with and look nicer later on

text_3class = {'train':[x['text'] for x in data_3class['train']], 
               'test':[x['text'] for x in data_3class['test']]}

labels_3class ={'train':[x['label'] for x in data_3class['train']],
                'test':[x['label'] for x in data_3class['test']]}

nb_nlp = {'smal': spacy.load('nb_core_news_sm'), 
          'medium': spacy.load('nb_core_news_md'), 
          'large':spacy.load('nb_core_news_lg')}

file_1 = open('stopwords-no.json')
file_2 = open('stopwords_nb.txt')
no_stop = {'short': file_2.read().split('\n'), 'long':json.load(file_1)}

class lemmatizer:
    data = []
    nlp = spacy
    stop = []
    other = []

    def __init__(self, nlp:spacy = nb_nlp['smal'], stop:list = []):
        self.nlp = nlp
        self.stop = stop

    def fit(self, list_sentc:list, other:list):
        """takes a list of sentences and returns a list of lemmatized sentences

        Args:
            list_sentc (list): sentences

        Returns:
            list: lemmatized sentences
        """
        data = []
        for sentence in list_sentc:
            doc = self.nlp(sentence.lower())
            data.append(' '.join(
                [token.lemma_ for token in 
                 doc if token.lemma_ not in self.stop]))
        self.data = data
        self.other = other

    def get_params(self, deep=False):
        return {"nlp": self.nlp, "stop": self.stop}

    def set_params(self, **parameters):
        for parameter, value in parameters.items():
            setattr(self, parameter, value)
        return self

    def transform(self)->list:
        return self.data, self.other
    
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.pipeline import Pipeline

classifiers =[
    LogisticRegression(n_jobs=-1),
    MLPClassifier(),
    KNeighborsClassifier(n_jobs=-1),
    SVC(),
    GaussianProcessClassifier(n_jobs=-1),
    RBF(),
    DecisionTreeClassifier(),
    RandomForestClassifier(n_jobs=-1),
    AdaBoostClassifier(),
    GradientBoostingClassifier(),
    GaussianNB(),
    MultinomialNB(),
    BernoulliNB()
]

text = text_3class['train'] + text_3class['test']
labels = labels_3class['train'] + labels_3class['test']

for clf in classifiers:
    pipe = Pipeline([
        ("lem", lemmatizer()),
        ("vct", TfidfVectorizer()),
        ("clf", clf)])
    
    parms = {"lem__stop": [[] ,no_stop['short'], no_stop['long']],
            "lem__nlp": [nb_nlp['smal'], nb_nlp['medium'], nb_nlp['large']],
            "vct__use_idf": [True, False],
            "vct__ngram_range": [(1,1), (1,2), (1,3)]}

    try:
        grid = GridSearchCV(pipe, parms, n_jobs=-1)
        grid.fit(text, labels)
    except:
        continue

    score = grid.best_score_
    estimator = grid.best_estimator_
    
    print(clf, score, estimator, sep='\n')

# CountVectorizer, tokenizes, builds a vocabulary, and encodes the text, in other words, it seperates sentences into lists of words, removes norwegian stopwords (due to us defining norwegian stopwords), and builds dictionaries of the frequencie of each word across each sentence. the stoppwords used here are downloaded from the git: https://raw.githubusercontent.com/stopwords-iso/stopwords-no/master/stopwords-no.json

# The transform function turns the dictionaries from "CountVectorizer" into vectors, and the "get_feature_names_out" function returns the words in the two vectors as a list in alphabetical order. we see that the vectors build on lemmatized sentences are smaler

# still need to test neural network accuracy, and find the optimal classifier for binary sentiment analysis


