fname = input('enter a file name: ')
try:
    fhand = open(fname)
except:
    print('Not a file name!')
    quit()

counts = dict()

for line in fhand:
    if line[:4] == 'From':
        words = line.split()
        mail_dom = words[1].split('@')
        if mail_dom[1] not in counts:
            counts[mail_dom[1]] = 1
        else:
            counts[mail_dom[1]] += 1

for i in counts:
    counts[i] = int(counts[i]/2)
print(counts)