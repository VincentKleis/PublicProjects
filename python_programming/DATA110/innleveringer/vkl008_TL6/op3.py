def fjern_vokaler(fil_navn:str)-> str:
    vokaler = ['a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å']

    with open(fil_navn, 'r', encoding='UTF-8') as f:
        text = f.read()

    for n in vokaler:
        text = text.replace(n, '')
    print(text)
    
    with open('ny_'+fil_navn, 'w', encoding='UTF-8') as f:
        f.write(text)
    
# test
fjern_vokaler('tre_små_kinesere.txt')
