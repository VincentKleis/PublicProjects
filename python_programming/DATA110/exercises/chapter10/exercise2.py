fname = input('Enter a file name: ')
try:
    with open(fname) as fhand:
        flines = fhand.readlines()
except:
    print(f'{fname} is not an aceptable file name')

dates = {}

for lines in flines:
    line = lines.split()

    if len(line) != 0 and line[0] == 'From':
        date = line[5].split(':')

        if date[0] not in dates:
            dates[date[0]] = 1
        else:
            dates[date[0]] += 1

result = []

for key, val in dates.items():
    result.append( (key, val) )

result.sort()

for val, key in result:
    print(val, key)