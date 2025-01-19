from torchkge.utils.datasets import load_fb15k237




kg_train, kg_val, kg_test = load_fb15k237(data_home='users/vincentkleis/datasets_knowledge_embedding')

print(list(kg_train.ent2ix.keys())[-10:])
print(list(kg_train.rel2ix.keys())[-10:])


# Download files with human-readable labels for (most) Freebase entities used in the dataset. Labels seem to be missing # for some entities used in FB15k-237.
import json

# mac
TEXT_TRIPLES_DIR = '/Users/vincentkleis/datasets_knowledge_embedding/FB15k-237/'
with open(TEXT_TRIPLES_DIR+'entity2wikidata.json') as file:
    _entity2wikidata = json.load(file)

    ent2lbl = {
        ent: wd['label']
        for ent, wd in _entity2wikidata.items()
}

lbl2ent = {lbl: ent for ent, lbl in ent2lbl.items()}


print([
    ent2lbl[ent] 
    for ent in kg_train.ent2ix.keys()
    if ent in ent2lbl][-10:])

print(lbl2ent)