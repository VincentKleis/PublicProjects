fhand = open('exercises\chapter9\mbox-short.txt')

counts = dict()
for line in fhand:
    words = line.split()

    if 'From' in words:
        if words[2] not in counts:
            counts[words[2]] = 1
        else:
            counts[words[2]] += 1

print(counts)