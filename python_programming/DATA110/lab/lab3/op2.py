navn = input('Ditt navn: ')
alder = int(input('Din alder: '))
kjønn = input('Kjønn, M/K: ')
n_barn = int(input('Anntal barn: '))
vandel = int(input('Vandel, på skala fra 1(dårlig) til 9(plettfri): '))
rulleblad = input('Rulleblad (straffet/tiltalt/mistenkt/rent): ')
ansiennitet = int(input('Ansiennitet (år): '))
forvekslbare_navn = ['kristen', 'kim', 'janne', 'tony']

navn = navn.lower()
kjønn = kjønn.upper()
rulleblad = rulleblad.lower()

if kjønn == 'M' or alder < 20 or vandel < 5:
    kvalifikasjon = 'Ukvalifisert'

elif n_barn == 0 and alder < 30:
    kvalifikasjon = 'Støttemedlem \nSoldat'
    if ansiennitet > 4 and rulleblad != 'rent':
        kvalifikasjon = kvalifikasjon + '\nSersjant'

elif alder < 40 and ansiennitet > 5 and rulleblad == 'tiltalt' or rulleblad == 'straffet':
    kvalifikasjon = 'Kaptein'
    if alder < 30:
        kvalifikasjon ='Støttemedlem \nSoldat \nSersjant \n' + kvalifikasjon
    if rulleblad == 'straffet' and vandel > 3:
        kvalifikasjon = kvalifikasjon + '\nKomandant'
        if ansiennitet > 7 and navn not in forvekslbare_navn:
            kvalifikasjon = kvalifikasjon + '\nPresident'

print(f'{navn.capitalize()} er kvalifisert for:\n {kvalifikasjon}')
