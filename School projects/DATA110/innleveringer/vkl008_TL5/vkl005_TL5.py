# op 1
def antall_vokaler(x):
    n = 0
    vokaler = ['a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å']
    for i in x:
        if i in vokaler:
            n += 1
    return n

# op 2
# test
print(antall_vokaler('Tre små kinesere på Høybro plass'))

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