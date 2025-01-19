navn_f = input('Hva er ditt fornavn? ')
navn_e = input('Hva er ditt etternavn? ')
navn_m = input('Hva er ditt mellomnavn? (om du ikke har mellomnavn trykk enter) ')

def fulltnavn(navn_f, navn_e, navn_m):
    if navn_m != '':
        fulltnavn = f'ditt navn er fulle: {navn_f} {navn_m} {navn_e}'
    else:
        fulltnavn = f'ditt navn er fulle: {navn_f} {navn_e}'

    return fulltnavn

print(fulltnavn(navn_f, navn_e, navn_m))
