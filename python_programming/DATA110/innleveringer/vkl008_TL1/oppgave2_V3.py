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
