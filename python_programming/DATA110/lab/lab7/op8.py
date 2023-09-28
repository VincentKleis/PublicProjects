konge_familie = \
['Kong Otto', 'dronning Magda','Kronprins Ulf', \
'kronprinsesse Frida','prinsesse Angela', \
'Prins Peter', 'prinsesse Petra','grevinne Gunda', \
'Grev Wilhelm', 'Prins Ingolf']
def prinser_og_prinsesser(konge_familie):
    result = []
    for i in konge_familie:
        if i[:5] == 'Prins':
            result.append(i[6:])
        if i[:9] == 'prinsesse':
            result.append(i[10:])
    return '\n'.join(result)

print(prinser_og_prinsesser(konge_familie))