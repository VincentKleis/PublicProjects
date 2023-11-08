import random

jeg = input('1=stein, 2=saks, 3=papir: ')           #ber om tall mellom 1 og 3
maskin = random.randint(1,3)                        #genererer ett tilfeldig tall mellom 1 og 3

try:
    jeg=int(jeg)
    jeg == 1 or jeg == 2 or jeg == 3
except:
    print('ikke ett heltall\n prøv på nytt')        #tester om vi oppererer med et heltall mellom 1 og 3

jeg=int(jeg)                                        #gjør 'jeg' om til et heltall
print(maskin)


while maskin == jeg:
    print(f'maskin:{maskin}\nuavgjort, prøv igjen!') #hvis uavgjort ender du i en loop til du ikke er uavgjort lenger
    jeg = int(input('1=stein, 2=saks, 3=papir: '))
    maskin = random.randint(1,3)

if maskin==1:
    print('maskin: stein')
elif maskin==2:
    print('maskin: saks')                           #gir maskinen sit valg et navn som ikke er ett tall
else:
    print('maskin: papir')

if (jeg+1 == maskin) or (jeg == 3 and maskin == 1):
    print('du vant!')                                #finner resultatet og forteller det til brukeren
else:
    print('maskinen vant.')
