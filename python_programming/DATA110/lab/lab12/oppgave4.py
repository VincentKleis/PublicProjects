import string
class kryptering:
    alfabet = 'abcdefghijklmnopqrstuvwxyzæøå'

    def __init__(self, n:int):
        self.n = n
        self.kode = self.alfabet
        for i in range (0, n):
            self.kode = self.kode[1:len(self.alfabet)] + self.kode[0]
        self.alfabet += string.punctuation + ' '
        self.kode +=    string.punctuation + ' '

    def krypter(self, tekst:str)->str:
        resultat = ''
        for bokstav in tekst:
            resultat += self.kode[self.alfabet.index(bokstav)]
        return resultat

    def dekrypter(self, tekst:str)->str:
        resultat = ''
        for bokstav in tekst:
            resultat += self.alfabet[self.kode.index(bokstav)]
        return resultat

#test
dag1 = kryptering(21)
test1 = dag1.krypter('python')
test2 = dag1.dekrypter(test1)
print(test1, test2, sep='\n')