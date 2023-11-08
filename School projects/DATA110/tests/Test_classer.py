class Person:
    def __init__(self):
        self.navn = ""
        self.telefon = "" 

    def vis(self):
        print(f'{self.navn} {self.telefon}')

Person().vis()
