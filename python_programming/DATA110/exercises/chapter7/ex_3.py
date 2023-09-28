from typing import Counter


fname = input('Enter the file name:')
count = 0
if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - you have been punk'd")
    exit()
try:
    fhand = open(fname)
    for line in fhand:
        count += 1
    print(f'There where {count} lines in {fname}')
except:
    print(f'File with the name {fname} can not be found')
    exit()
