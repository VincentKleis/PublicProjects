def skriv_navn(navn):
    navn_list = navn.split(' ')
    fornavn = navn_list.pop(0)
    etternavn = navn_list.pop(-1)
    mellomnavn = []
    for i in navn_list:
        mellomnavn.append(i[:1])
    officielt = [f'{etternavn},', fornavn] + mellomnavn
    print(' '.join(officielt))
skriv_navn('Tara Estelle Cybele Bergerud von-Chantz')