fhand = open('mbox-short.txt')
count = 0
day_of_week = ['Mon', 'Thu', 'Wed', 'Tue', 'Fri', 'Sat', 'Sun']
for line in fhand:
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        for i in words:
            if i in day_of_week:
                print(words[words.index(i)])