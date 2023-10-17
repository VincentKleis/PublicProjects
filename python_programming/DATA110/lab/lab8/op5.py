from typing import Counter


class konto:
    kontonummer=None
    innehaver=None
    saldo=None

    def __init__(self,kontoNr, innehaver,saldo):
        self.kontonummer=kontoNr
        self.innehaver=innehaver
        self.saldo=saldo

    def skriv(self):
        print(str(self.kontonummer)+'/'+ \
                self.innehaver+' : '+ \
                str(self.saldo))
    
    def innskudd(self):


kontoer=[] #Listen holder kontoene gjennom dagen

def lesKontoer(): #Leser inn kontolisten hver morgen
    global kontoer
    kontofil=open('kontoer.txt')
    while True:
        kontonummer=kontofil.readline().strip()
        if kontonummer=='':break #lest alt
        innehaver=kontofil.readline().strip()
        saldo=kontofil.readline().strip()
        kontoer.append(konto(int(kontonummer), \
                        innehaver, \
                        int(saldo)))
    kontofil.close()

def lagreKontoer(): #Lagrer kontolisten hver kveld
    kontofil=open('kontoer.txt','w')
    for k in kontoer:
        kontofil.write(str(k.kontonummer)+'\n')
        kontofil.write(k.innehaver+'\n')
        kontofil.write(str(k.saldo)+'\n')
        kontofil.close()

def start():
    Counter = 1
    while True:
        print('''
---------------------
Velg handling (? for valgmeny)
1 - Opprett ny konto
2 - Innskudd
3 - Uttak
4 - Kontoutskrift
5 - Kontooversikt for kunde
6 - Avslutt
---------------------
    ''')
        tast = input('Velg>')
        if tast == '1':
            konto(Counter, input('Innehaver: '), input('Startinnskud: '))
        if tast == '2':
            