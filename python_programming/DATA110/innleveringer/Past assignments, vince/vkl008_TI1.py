        #Oppgave 1
#første måte å gjøre det på
print('Vincent\nSickinghe\nKleis')
#andre måte å gjøre det på
print('Vincent')
print('Sickinghe')
print('Kleis')

        #Oppgave 2
#her tester jeg tre måter å gjøre det på
print('*           *  *  *     *    **  *******  *     *  *******')
print(' *         *   *  **    *   *    *        **    *     *   ')
print('  *       *    *  * *   *  *     *        * *   *     *   ')
print('   *     *     *  *  *  *  *     ******   *  *  *     *   ')
print('    *   *      *  *   * *  *     *        *   * *     *   ')
print('     * *       *  *    **   *    *        *    **     *   ')
print('      *        *  *     *    **  *******  *     *     *   ')
#ganske strait forward

#prøver å spare tegn ved å fjerne alle 'print()'funksjonene
print('\
*           *  *  *     *    **  *******  *     *  *******\n\
 *         *   *  **    *   *    *        **    *     *   \n\
  *       *    *  * *   *  *     *        * *   *     *   \n\
   *     *     *  *  *  *  *     ******   *  *  *     *   \n\
    *   *      *  *   * *  *     *        *   * *     *   \n\
     * *       *  *    **   *    *        *    **     *   \n\
      *        *  *     *    **  *******  *     *     *   ')
#denne metoden brukte 34 ferre tegn en versjon1

st7 = '*******' #jeg så at både E-en og N-ene i navnet mitt var reppetetive.
st6 = '****** ' #derfor skapte jeg disse 10 variabelene for å spare tegn.
sp6 = '*      ' #'st' står for stjerne og 'sp' for space.
n1 = '*     *'  #siden det er to N-er i navnet mitt
n2 = '**    *'  #sparer jeg litt plass på å bruke variabler for ver linje med N
n3 = '* *   *'
n4 = '*  *  *'
n5 = '*   * *'
n6 = '*    **'
n7 = '*     *'
print('\
*           *  *',n1 ,'  **',st7 ,n1 ,'*******\n\
 *         *   *',n2 ,' *  ',sp6 ,n2 ,'   *   \n\
  *       *    *',n3 ,'*   ',sp6 ,n3 ,'   *   \n\
   *     *     *',n4 ,'*   ',st6 ,n4 ,'   *   \n\
    *   *      *',n5 ,'*   ',sp6 ,n5 ,'   *   \n\
     * *       *',n6 ,' *  ',sp6 ,n6 ,'   *   \n\
      *        *',n7 ,'  **',st7 ,n7 ,'   *   ', sep = '  ')
#sep spare meg kun der det må være et comma for å kunne putte in en variabel;
#det gir meg også muligheten til hurtig angi avstanden mellom bokstavene.
#det mest ironiske er at jeg brukte 87 ekstra tegn i denne versjonen;
#dersom jeg hadde skrevet resten av navnet mitt ville det sansynligvis spart tegn.

        #Bonus
#Hele navnet mitt i samme format:
st7 = '*******' #E er en blanding av 7 stjerne 6 stjerner og 1 stjerne med 6 mellomromm
st6 = '****** ' #E kan formuleres som st7, sp6, sp6, st6, sp6, sp6, st7.
sp6 = '*      '
s5t = '*     *'
                #H kan skapes med bare "7 stjerner" og "1 stjerne 5 mellomromm 1 stjerne"
c1 = '   ****'  #toppen og bunnen på C er like
c2 = ' **    '
c3 = '*      '

g6 = ' **   *'  #topp 3 linjene av G er de samme som i C, og 4de linje er samme som st7
g7 = '   *** '  #g5 er samme som s5t

i1 = '*'  #I er bare en vertikal linje linje

k2 = '*   ** '  #toppen og bunnen av K er samme som s5t
k3 = '* **   '
k4 = '**     '  #k5 og k6 er samme som henholdsvis k2 og k3
                #L består bare av st7 og sp6
n2 = '**    *'  #toppen og bunnen av N berstår av s5t
n3 = '* *   *'
n4 = '*  *  *'
n5 = '*   * *'
n6 = '*    **'

s4 = ' ***** '  #toppen av S er det samme som de første 3 linjene av C
s5 = '      *'
s6 = '    ** '
s7 = '****   '

s1s = '   *   ' #'space'1'space' og st7 er det eneste vi trenger for T

v3 = ' *   * '  #annen vær linje er lik med den før, toppen er samme som s5t, og bunnen s1s.
v5 = '  * *  '  #V bygges da: s5t, s5t, v3, v3, v5, v5, s1s.
print('',\
    s5t, i1, s5t, c1, st7, s5t, st7, '\n',\
    s5t, i1, n2 , c2, sp6, n2 , s1s, '\n',\
    v3 , i1, n3 , c3, sp6, n3 , s1s, '\n',\
    v3 , i1, n4 , c3, st6, n4 , s1s, '\n',\
    v5 , i1, n5 , c3, sp6, n5 , s1s, '\n',\
    v5 , i1, n6 , c2, sp6, n6 , s1s, '\n',\
    s1s, i1, s5t, c1, st7, s5t, s1s, '\n\n',\
    c1, i1, c1 , s5t, i1, s5t, c1 , s5t, st7, '\n',\
    c2, i1, c2 , k2 , i1, n2 , c2 , s5t, sp6, '\n',\
    c3, i1, c3 , k3 , i1, n3 , c3 , s5t, sp6, '\n',\
    s4, i1, c3 , k4 , i1, n4 , st7, st7, st6, '\n',\
    s5, i1, c3 , k3 , i1, n5 , s5t, s5t, sp6, '\n',\
    s6, i1, c2 , k2 , i1, n6 , g6 , s5t, sp6, '\n',\
    s7, i1, c1 , s5t, i1, s5t, g7 , s5t, st7, '\n\n',\
    s5t, sp6, st7, i1, c1, '\n',\
    k2 , sp6, sp6, i1, c2, '\n',\
    k3 , sp6, sp6, i1, c3, '\n',\
    k4 , sp6, st6, i1, s4, '\n',\
    k3 , sp6, sp6, i1, s5, '\n',\
    k2 , sp6, sp6, i1, s6, '\n',\
    s5t, st7, st7, i1, s7, '\n',\
    sep = '  ')

        #Oppgave3
        #a)
nok = 250           #siden vi ikke har gått gjennom input nøkkelordet,
                    #bruker jeg en variabel du må inn i filen for å endre.
eur = nok * 0.098
dol = nok * 0.12    # tallene i 'eur' og 'dol' variabelene er veriden av 1 krone i dollar eller euro.
print(nok,'Kroner tilsvarer',eur,'Euro og',dol,'Dollar')

        #b)
nok = 250           #siden vi ikke har gått gjennom input nøkkelordet bruker jeg det ikke;
eur = nok * 0.098   #dette er grunden til at man må in her og modifisere ved siden av nok variabelen.
dol = nok * 0.12    #tallene i 'eur' og 'dol' variabelene er veriden av 1 krone i dollar eller euro.
print('NOK ',nok,' tilsvarer ' ,eur, u"\N{euro sign}",' og '
                               ,dol, u"\N{dollar sign}",sep = '') #sepparert så det er lettere å sammenligne spesial koden.
                               #'sep' opsjonen er til for å fjerne avstanden mellom dollar og eurotegnet og verdiene.
