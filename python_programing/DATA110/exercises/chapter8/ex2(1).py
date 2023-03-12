fhand = open('mbox-short.txt')
coun = 0
day_list = ['Fri', 'Thu', 'Thi', 'Wed', 'Mon', 'Sat', 'Sun']
for line in fhand:
    words = line.split()
    # print('Debug: ', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    if any(x in words[2] for x in day_list):
        print(words[2])