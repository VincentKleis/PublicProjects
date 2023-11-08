
emner = []

karakterer = {}
try:
    with open('vkl008_HI2\Fag og karakterer.txt', 'r') as fhand:
        for line in fhand:
            line = line.split()
            try:
                if line[0] not in emner:
                    emner.append(line[0])
                if line[0] not in karakterer:
                    karakterer[line[0]] = line[1]
                continue
            except:
                continue
except:
    emner = ['ECON100', 'ECON110', 'ECON130', 'ECON240', 'ECON115', 'ECON116', 'ECON140', 'DATA110', 'INFO104', 'ECON224']
    karakterer = {'ECON100': 'E', 'ECON110' : 'D', 'ECON130' : 'D', 'ECON240' : 'E', 'ECON116' : 'E', 'ECON140' : 'D'}




def start():
    print(karakterer)
    print(emner)
    navn_til_kode = {   'økonomi' : 'ECON', 'informasjonsvitenskap' : 'INFO', 'datafag' : 'DATA', 
                            '1' : 'F', '2' : 'E', '3' : 'D', '4' : 'C', '5' : 'B', '6': 'A'}
    
    kode_til_tall = {'F' : 1 , 'E' : 2, 'D' : 3, 'C' : 4, 'B' : 5, 'A' : 6}

    def snitt_regner(kode: str, fag: str) -> str:
        """tar i mot parameter og regner på snittet til fagene som faller innenfor de parameterene

        Args:
            kode (str): tall del av fagkode 
            fag (str): tekst del av fagkode

        Returns:
            int: snitt
        """
        nonlocal kode_til_tall, navn_til_kode

        karakter_liste =[]

        liste = emne_velger(kode, fag)

        for i in liste:
            i = i.split()
            try:
                if i[1] in kode_til_tall:
                    karakter_liste.append(kode_til_tall[i[1]])
            except:
                continue
        return navn_til_kode[str(round(sum(karakter_liste)/len(karakter_liste)))]
        

    def emne_velger(kode: str, fag: str) -> list:
        """Printer listen med karakterer basert på parametere

        Args:
            kode (str): tall del av fagkode 
            fag (str): tekst del av fagkode

        Returns:
            list: alle fag og karakterer som matcher inputt parameterene
        """
        nonlocal navn_til_kode
        
        output_list = []

        for i in emner:
            #oversetter kode og eller fag hvis de er nøkler i "navn_til_kode"
            if fag in navn_til_kode:
                fag = navn_til_kode[fag]

            if kode in navn_til_kode:
                kode = navn_til_kode[kode]

            if kode != '' and i[-3] != kode[0]:
                continue
            elif fag != '' and fag != i[:-3]:
                continue
            elif i in karakterer:
                output_list.append(f'{i} {karakterer[i]}')
            else:
                output_list.append(i)
                    
        return output_list

    def lagre():
        with open('vkl008_HI2\Fag og karakterer.txt', 'w') as fhand:
                for i in emne_velger('', ''):
                    fhand.write(f'{i}\n')

    meny = ('''--------------------
1 Emneliste
2 Legg til emne
3 Sett karakter
4 Karaktersnitt
5 Avslutt
6 Lagre
--------------------''')
    print(meny)
    while True:
        valg = input('Velg handling (0 for meny) ')

        if valg == '0':
            print(meny)
            continue

        if valg == '1':
            print('Velg fag og/eller emnenivå (<enter> for alle)')
            fag = input(' - Fag: ')
            nivå = input(' - Nivå: ')
            print(*emne_velger(nivå, fag), sep='\n')

        if valg == '2':
            emne = input('Nytt emne: ')
            emner.append(emne)
            karakterer[emne] = ''

        if valg == '3':
            emne = input('Emne: ')
            karakter = input('Karakter (<enter> for å slette): ')
            karakterer[emne] = karakter

        if valg == '4':
            print('Velg fag og/eller emnenivå (<enter> for alle)')
            fag = input(' - Fag: ')
            nivå = input(' - Nivå: ')
            try:
                print(snitt_regner(nivå, fag))
            except:
                print('Du har ingen karaktere i de fagene')

        if valg == '5':
            slutvalg = input('Vil du lagre endringene? (j/n) ')
            if slutvalg == 'j':
                lagre()
            quit()

        if valg == '6':
            lagre()

start()