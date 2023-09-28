with open('telefon.txt') as f:
    telefon_list = f.read()

with open('adresse.txt') as f:
    adresse_list = f.read()

data = []

for line in telefon_list.split('\n'):
    line = line.split()

    for i in adresse_list.split('\n'):
        i = i.split()

        if len(line) != 0 and len(i) != 0 and line[0] == i[0]:
            adresse = i[1:]
            line.append(' '.join(adresse))

    data.append(line)

with open('kontaktinfo.txt', 'w') as f:
    for line in data:
        f.write(' '.join(line)+'\n')
