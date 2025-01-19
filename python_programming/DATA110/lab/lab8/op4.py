def erstatt_sifre(fil_navn:str):
    tall_ord = {
        '0':'null',
        '1':'en', 
        '2':'to', 
        '3':'tre', 
        '4':'fire', 
        '5':'fem', 
        '6':'seks', 
        '7':'syv', 
        '8':'åtte', 
        '9':'ni'}
    with open(fil_navn, 'r') as f:
        telefon = f.read()

        for n in tall_ord:
            telefon = telefon.replace(n, tall_ord[n]+' ')
    
    with open('nyt_'+fil_navn, 'w', encoding='utf-8') as f:
        f.write(telefon)

# test
erstatt_sifre('telefon.txt')