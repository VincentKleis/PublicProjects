import random

spar = '\u2660'
ruter = '\u2666'
kløver = '\u2663'
hjerter = '\u2665'
mulig_tall = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def tilf_kort(farg = random.choice([spar, ruter, kløver, hjerter])):
    """Funciton acsepts 4 suits, or chooses one at random

    Args:
        farg ([Var], optional): [suit of card]. Defaults to random.choice([spar, ruter, kløver, hjerter]).

    Returns:
        [string]: [suit + number]
    """
    return farg + random.choice(mulig_tall)


#program start

print(tilf_kort())
print(tilf_kort(spar))
print(tilf_kort(ruter))
print(tilf_kort(kløver))
print(tilf_kort(hjerter))