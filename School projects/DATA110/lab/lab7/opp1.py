def skriv_navn(navn):
    fornavn = navn[0: navn.index(' ')]
    mellom_etter = navn[navn.index(' ')+ 1:]
    etternavn = mellom_etter[-mellom_etter.index(' ')+ 4:]
    mellomnavn = mellom_etter[:1]
    fullnavn = f'{etternavn}, {fornavn} {mellomnavn}'
    print(fullnavn)
skriv_navn('Vincent Sickinghe Kleis')