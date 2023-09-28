C = u"\N{degree celsius}"
F = u"\N{degree fahrenheit}"
def temp_konv(tall, scala = 'C'):
    if scala == 'C':
        return f'{tall} grade {C}  er {tall*(9/5)+32} {F}'
    elif scala == 'F':
        return f'{tall} grade {F}  er {(tall-32)*5/9} {C}'

###########################
##########TEST#############
print(temp_konv(34,'C'))
print(temp_konv(93.2,'F'))
print(temp_konv(34))