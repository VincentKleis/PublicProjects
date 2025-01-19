TV= \
'''
Tulleveien Velforening
leder: Kari
kasserer: Ole
IT-ansvarlig: Liv
parkeringsansvarlig: Kari
arrangementsansvarlig: Liv
hagekonsulent: Kari
branna
'''
def verv(navn):
    str_list = TV.splitlines()
    stillinger = [x[0:-len(navn)-2] for x in str_list if x[-len(navn):]== navn]
    return stillinger

# test
print(verv('Kari'))
