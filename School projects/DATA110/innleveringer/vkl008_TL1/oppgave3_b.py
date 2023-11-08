nok = 250           #siden vi ikke har gått gjennom input nøkkelordet bruker jeg det ikke;
eur = nok * 0.098   #dette er grunden til at man må in her og modifisere ved siden av nok variabelen.
dol = nok * 0.12    #tallene i 'eur' og 'dol' variabelene er veriden av 1 krone i dollar eller euro.
print('NOK ',nok,' tilsvarer ' ,eur, u"\N{euro sign}",' og '
                               ,dol, u"\N{dollar sign}",sep = '') #sepparert så det er lettere å sammenligne spesial koden.
