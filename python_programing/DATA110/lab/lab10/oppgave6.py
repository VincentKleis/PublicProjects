# a)
with open('lab\lab10\Bøker.txt', 'r', encoding='utf8') as fhand:
    bøker = fhand.readlines()
    bøker = [tuple(i.rstrip().split(' , ')) for i in bøker]

def skriv_bøker(bøker:list) -> str:
    for i in bøker:
        print(*i, sep = ' , ')


skriv_bøker(bøker)
print(bøker)

# b)
def legg_til_bøker():
    forfatter = input('Forfatter: ')
    tittel = input('Tittel: ')
    fagfelt = input('Fagfelt: ')
    utgivelser = input('Utgivelsesår: ')
    bøker.append(f'{forfatter} , {tittel} , {fagfelt} , {utgivelser}\n')
    bøker.sort()
    return bøker

legg_til_bøker()
skriv_bøker(bøker)

# c)
def finn_forfatter(navn: str) -> str:
    for i in bøker:
        if i[0] == navn:
            print(*i[1:], sep = ' , ')

finn_forfatter('Dowek')

# d)
def finn_fagfelt(fagfelt: str) -> str:
    for i in bøker:
        if i[2] == fagfelt:
            print(*i[:2], i[3], sep = ' , ')

finn_fagfelt('filosofi')
