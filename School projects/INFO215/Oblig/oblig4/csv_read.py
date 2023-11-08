from newspaper import Article
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

csv_in_path = '20230317141500.export.CSV'

with open(csv_in_path) as csv:
    content = csv.readlines()

links = []

for line in content:
    for sentence in line.split('\t'):
        if sentence[-1:] == '\n':
            if sentence[:-1] not in links:
                links.append(sentence[:-1])
            else:
                continue


with open('out.csv', 'w') as out:
    out.write('Article link, Entities\n')

nlp = spacy.load('en_core_web_lg')
pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']

for link in links:
    try:
        article = Article(link)
        article.download()
        article.parse()
        article.nlp()
    except:
        continue

    
    article_text = article.summary

    doc = nlp(article_text)
    
    with open('out.csv', 'a') as out:
        entities = [ent.text for ent in doc 
                    if ent.text not in STOP_WORDS 
                    and ent.text not in punctuation
                    and ent.pos_ in pos_tag]
        str_ents = ', '.join(entities)
        out.write(f'{link}, {str_ents}\n')  