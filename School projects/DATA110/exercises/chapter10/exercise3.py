import string
fname = input('File name: ')
try:
    with open(fname) as fhand:
        flines = fhand.readlines()
except:
    print(f'{fname} is not a file we can find')

letter_freq = {}
numbers = '0123456789'

for line in flines:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', numbers))
    line = line.lower()
    words = line.split()
    for i in words:
        i = list(i)
        for x in i:
            if x not in letter_freq:
                letter_freq[x] = 1
            else:
                letter_freq[x] += 1

result = []

for key, val in letter_freq.items():
    result.append( (val, key) )

result.sort()

for val, key in result:
    print(key, val)