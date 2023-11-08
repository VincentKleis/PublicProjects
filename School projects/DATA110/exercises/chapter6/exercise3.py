def count(a, b):
    count = 0
    for letter in a:
        if letter == b:
            count = count + 1       #tar imot stening (a) og teller antal bokstaver (b)
    return count

word = input('Give me a word: ')
letter = input('Give me a letter: ')
print(f'there is {count(word,letter)} {letter} in {word}')
