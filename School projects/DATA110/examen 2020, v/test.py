fil = open('examen 2020, v\personer.txt')
P=None

class person:
    def __init__(self, f, e) -> None:
        self.fornavn = f
        self.etternavn = e
        self.n = None
    
    def skriv(self):
        x = P
        while x!=None:
            if x.fornavn==self.fornavn:
                print(x.fornavn,x.etternavn)
            x=x.n
    
for l in fil:
    (x,y)=l.split()
    p=person(x,y)
    p.n=P
    P=P
fil.close()
P.skriv()