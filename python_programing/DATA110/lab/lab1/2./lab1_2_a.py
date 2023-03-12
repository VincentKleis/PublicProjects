    #i
antallStudenter = 55
antallKvinner = 32
kvinneAndel = AntallKvinner/antallStudenter #syntaktisk feil stor A i AntallKvinner når det skulle vert liten
print('kvinneandelen er ', kvinneAndel)
    #ii
antallStudenter = 55
antallKvinner = 32
kvinneAndel = antallKvinner/antallStudenter
print(kvinneandelen er , kvinneAndel) #syntaktisk feil, mangler hermetegn rundt 'kvinner er'
    #iii
antallStudenter = 55
antallKvinner = 32
kvinneAndel = antallKvinner/antallStudenter
print('kvinneandelen er ' kvinneAndel) #syntaktisk feil, mangler komma mellom string og variabel
    #iv
kvinneAndel = antallKvinner/antallStudenter
antallStudenter = 55
antallKvinner = 32
print('kvinneandelen er ', kvinneAndel) #logisk feil, 'kvinneAndel' variabelen er for tidlig.
    #v
kvinneAndel = antallKvinner=32)/(antallStudenter=55 #syntaktisk feil, kan ikke definere variabler i variabler
print('kvinneandelen er ', kvinneAndel)
    #vi
antallStudenter = 55
antallKvinner = 32
kvinneAndel = antallStudenter/antallKvinner
print('kvinneandelen er ', kvinneAndel) #semantisk feil, finner andel studenter og ikke andel kvinner
