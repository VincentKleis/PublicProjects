fname = input('enter a file name: ')
try:
    with open(fname) as fhand:
        fline = fhand.readlines()
except:
    print(f'{fname} is not a file name!')
    quit()

counts_mail = {}

for line in fline:
    line = line.split()
    if len(line) != 0 and line[0] == 'From':
        if line[1] not in counts_mail:
            counts_mail[line[1]] = 1

        else:
            counts_mail[line[1]] += 1

lst = list()
for key, val in list(counts_mail.items()):
    lst.append((val,key))

lst.sort(reverse = True)

for key, val in lst[:1]:
    print(key, val)