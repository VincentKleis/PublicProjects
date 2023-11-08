# lag en funksjon som finner den siste verdien i en string, liste eller intervall

def siste(x):
    y = x[-1]
    return y

test1 = siste('Python')
test2 = siste([1,2,3,4,5])
test3 = siste(range(90,100))
print(test1, test2, test3, sep = '\n')