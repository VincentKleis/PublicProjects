class kryptering:
    alfabet = 'abcdefghijklmnopqrstuvwxyzæøå'

    def __init__(self, n:int):
        self.kode = self.alfabet
        for i in range(0, n): 
            print(self.kode)
            self.kode = self.kode[1:len(self.alfabet)] + self.kode[0]

    def krypter(self, tekst:str)->str:
        resultat = ''
        for bokstav in tekst:
            resultat = resultat + self.kode[self.alfabet.find(bokstav)]
        return resultat
    
    def dekrypter(self, tekst:str)->str:
        resultat = ''
        for bokstav in tekst:
            resultat = resultat + self.alfabet[self.kode.find(bokstav)]
        return resultat

dag1 = kryptering(21)
test1 = dag1.krypter('python')
test2 = dag1.dekrypter(test1)
print(test1,test2,sep='\n')