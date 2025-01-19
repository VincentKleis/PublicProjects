# a)
TV= \
'''
Tulleveien Velforening
leder: Kari
kasserer: Ole
IT-ansvarlig: Liv
parkeringsansvarlig: Kari
arrangementsansvarlig: Liv
hagekonsulent: Kari
brannansvarlig: Kari
'''
def antall_verv(navn: str) -> int :
    """tar imot et navn, 
    deler så TV opp i en liste og sammenlinger navnet med hver gjenstand i listen,
    hvis gjenstanden matcher navnet så går en teller 1 i pluss

    Args:
        navn (str): navn på person med verv

    Returns:
        int: antal ganger de innehar et verv i TV strengen
    """
    TV_list = TV.split()
    antall_verv = 0
    for i in TV_list:
        if i == navn:
            antall_verv += 1
    return antall_verv

print(antall_verv('Kari'))
# b)
def innsett(navn: str, arbeid: list) -> str:
    TV_list = TV.splitlines()
    count = 0
    for line in TV_list:
        if count < 2 and arbeid[count] == line[:len(arbeid[count])]:
            TV_list[TV_list.index(line)] = f'{arbeid[count]}: {navn}'
            count += 1
    return '\n'.join(TV_list)

# test
TV=innsett('Per',['kasserer','hagekonsulent'])
print(TV)

