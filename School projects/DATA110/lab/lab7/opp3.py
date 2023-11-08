'''
3.
Fyll ut de tre manglende tilordningene slik at variablene a og b bytter innhold.
 a='hei'
 b='hopp'
 print(a,b)
 a= ...
 b= ...
 a= ...
 print(a,b)
>>>
hei hopp
hopp hei
'''
a='hei'
b='hopp'
print(a,b)
a= [a, b]
b= a[0]
a= a[1]
print(a,b)