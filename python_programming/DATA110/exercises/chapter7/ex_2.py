fname = input('enter name if the file you want to proses:')
fhand = open(fname)
spam_count=0
spam_total = 0 
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        spam_count += 1
        start = line.index(':')+1 
        spam_total += float(line[start:-1])

print(f'Average spam confidence: {spam_total/spam_count}')        