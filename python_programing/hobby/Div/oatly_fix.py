with open('HOBBY/TXT_files/words_beta.txt','r', encoding='iso8859') as words:
    dictionary = words.readlines()

word1 = []
word2 = []
word3 = []
word4 = []
word5 = []
word6 = []
word7 = []
word_num = 3
for i in dictionary:
    i=i.rstrip('\n')
    i = list(i)
    if len(i) == 3 and word_num <= 6:

        if word_num <= 4:
            word4.append(''.join(i))

        if i[1] == 't' and word_num <= 1:
            word1.append(''.join(i))

        if i[2] == 'r':
            word6.append(''.join(i))

    if len(i) == 4 and word_num <= 5:
        if word_num <= 3:
            word3.append(''.join(i))

        if word_num <= 5:
            word5.append(''.join(i))

        if i[3] == 'e' and word_num <= 2:
            word2.append(''.join(i))
            
    if len(i) == 6 and i[2] == 'u':
        word7.append(''.join(i))

count = 0
time = 0
while word_num <= 6:
    if word_num >= 2:
        with open('HOBBY\TXT_files\possbible_oatly.txt','r', encoding='utf8') as oatly:
            globals()[f'word{word_num}'] = oatly.readlines()
        for x in globals()[f'word{word_num}']:
            x = x.rstrip(' \n')
        globals()[f'word{word_num-1}'] == []

    posible_sentences = [f'{a} {b}\n' for a in globals()[f'word{word_num}'] for b in globals()[f'word{word_num+1}']]
    posible_sentences.sort()
    word_num += 1

    with open('HOBBY\TXT_files\possbible_oatly.txt','w', encoding='utf8') as oatly:
        oatly.writelines(posible_sentences)
    print(f'word{word_num-1}*word{word_num} is compleet')