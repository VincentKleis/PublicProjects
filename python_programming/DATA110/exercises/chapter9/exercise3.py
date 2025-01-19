fname = input('enter a file name: ')
try:
    print(fname)
    fhand = open(fname)
except:
    print('Not a file name!')
    quit()

counts = dict()

for line in fhand:
    if line[:4] == 'From':
        words = line.split()
        if words[1] not in counts:
            counts[words[1]] = 1
        else:
            counts[words[1]] += 1

for i in counts:
    counts[i] = int(counts[i]/2)
print(counts)