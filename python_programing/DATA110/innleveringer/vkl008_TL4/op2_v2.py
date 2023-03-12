# a)
class monark_a:

    def __init__(self, navn, nasjon, tiltredelse_ano):
        self.navn = navn
        self.nasjon = nasjon
        self.tiltredelse_ano = tiltredelse_ano
    def info_str(self):
        info_str = f'{self.navn} av {self.nasjon}, {self.tiltredelse_ano}'
        return info_str

haakon = monark_a('Kong Haakon VII','Norge', 1905)
olav = monark_a('Kong Olav V','Norge', 1957)
harald = monark_a('Kong Harald V','Norge', 1991)
kongerekke = [haakon.info_str(), olav.info_str(), harald.info_str()]
print(kongerekke)

# b)
class monark_b:
    etterfølger = None
    navn = None
    nasjon = None
    tiltredelse_ano = None
    info_dict = {'navn': navn, 'nasjon': nasjon,'tiltredelse_ano': tiltredelse_ano }
    def __init__(self, navn, nasjon, tiltredelse_ano):
        self.navn = navn
        self.nasjon = nasjon
        self.tiltredelse_ano = tiltredelse_ano
        self.info_dict = {'navn': navn, 'nasjon': nasjon,'tiltredelse_ano': tiltredelse_ano }

    def leg_til_etterfølger(self, person):
        self.etterfølger = person
        return self.etterfølger

    def print_familie(self):
        print(f'navn : {self.navn} \nnasjon : {self.nasjon} \ntiltredelse : {self.tiltredelse_ano}\n')

        if self.etterfølger:
            self.etterfølger.print_familie()

haakon = monark_b('Kong Haakon VII','Norge', 1905)
olav = monark_b('Kong Olav V','Norge', 1957)
harald = monark_b('Kong Harald V','Norge', 1991)
haakon.leg_til_etterfølger(olav)
olav.leg_til_etterfølger(harald)
haakon.print_familie()
