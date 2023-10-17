''' Lag en funksjon skrivSekvens(sekvens) som skriver ut elementene på en line,
adskilt av mellomrom. Eksempel:
>>> skrivSekvens('Python')
P y t h o n
>>> skrivSekvens([1,2,3,4,5])
1 2 3 4 5
>>> skrivSekvens(range(90,100))
90 91 92 93 94 95 96 97 98 99 '''

def skrivSekvens(input):
    y = [x for x in input]

test1 = skrivSekvens('Python')
test2 = skrivSekvens([1,2,3,4,5])
test3 = skrivSekvens(range(90,100))

print(test1, test2, test3, sep = '\n')
