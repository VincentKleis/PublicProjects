class kapasitet_vakt:
    total_kap = 0
    ledig_kap = 0

    def __init__(self, people : 0):
        self.total_kap = people
        self.ledig_kap = self.total_kap

    def ledig(self):
        print(self.ledig_kap)
        
    def innpas(self, x):
        if self.total_kap == 0:
            print('Rommet er fult!')
        elif self.ledig_kap > x:
            self.ledig_kap -= x
        else:
            print(f'For mange! slip in {self.ledig_kap}')
            self.ledig_kap = 0
        return self.ledig_kap

    def utpass(self, x):
        if self.total_kap < x:
            print(f'Er ikke så mange i rommet')

        self.ledig_kap += x
        return self.ledig_kap
    
    def avslutt(self):
        quit()

lokale1 = kapasitet_vakt(10)
lokale2 = kapasitet_vakt(15)
lokale1.innpas(4)
lokale2.innpas(5)
lokale2.innpas(2)
lokale1.ledig()
lokale2.ledig()
lokale1.innpas(9)
lokale1.ledig()
lokale1.utpass(5)
lokale1.ledig()