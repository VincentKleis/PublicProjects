filename = input('enter a file name:')
fhand = open(filename)
count = 0
for line in fhand:
    if line[:5] == 'From ':
        words = line.split()
        for i in words: 
            if '@' in i: sender = i
        print(sender)
        count += 1
print(f'There were {count} lines in {filename} that started with From')