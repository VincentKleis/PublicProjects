class konto:
    antall_kontoer=0 # for automatisk genererte kontonumre
    kontonummer=None
    innehaver=None
    saldo=None
    rentesats=None

    def __init__(self, innehaver,saldo=0, rentesats=1.5):
        konto.antallKontoer=konto.antallKontoer+1
        self.kontonummer=konto.antallKontoer
        self.innehaver=innehaver
        self.saldo=saldo
        self.rentesats=rentesats

    def __del__(self): #varsler hvis kontoen blir slettet
        print('VARSEL! konto nr', self.kontonummer, 'blir slettet')
        self.skriv()

    def skriv(self):
        print(self.kontonummer,'('+str(self.rentesats)+'):',\
        self.saldo, ', Innehaver: '+self.innehaver)

    def innskudd(self, beløp):
        self.saldo=self.saldo+beløp

    def uttak(self, beløp): #returnerer False dersom det ikke er dekning.
        if beløp>self.saldo:
            print('Ikke dekning')
            return False
        else:
            self.saldo=self.saldo-beløp
            return True

    def endre_rente(self, rente):
        self.rentesats = rente

    def renteoppgjør(self):
        self.saldo += self.saldo * self.rentesats

    def overføring(self, innehaver, beløp):
        innehaver.saldo += beløp
        self.saldo -= beløp

test_konto1 = konto('Jane', 1000)
test_konto2 = konto('Kriss', 10000)
test_konto1.endre_rente(2.0)
print(test_konto1.rentesats)
print(test_konto1.saldo)
print(test_konto2.saldo)
test_konto1.renteoppgjør()
test_konto2.renteoppgjør()
print(test_konto1.saldo)
print(test_konto2.saldo)