fhand = open('romeo.txt')
Words_of_romeo = []
for line in fhand:
    words = line.split()
    for i in words:
        if i not in Words_of_romeo:
            Words_of_romeo.append(i)
Words_of_romeo.sort()
print(Words_of_romeo)
