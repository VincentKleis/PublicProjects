fname = input('type filename:')
fhand = open(fname)
output = ''
for line in fhand:
    line = line.rstrip()
    print(line.upper())