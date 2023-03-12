'''
Lag en funksjon som kan hjelpe dørvakten på et utested å holde styr på hvor mange
gjester som er sluppet inn og sikre at antallet ikke overstiger kapasiteten i lokalet.
Kapasiteten skal være parameter til funksjonen, og vakten skal kunne angi antall
personer i hver gruppe som ankommer eller forlater lokalet. 
Eksempel:
>>> kapasitetVakt(10)
Noen ankommer - tast 1
Noen går - tast 2
Avslutt - 0
Ledig kapasitet: 10
> 1
Hvor mange kommer? 5
Ledig kapasitet: 5
> 1
Hvor mange kommer? 4
Ledig kapasitet: 1
> 2
Hvor mange går? 2
Ledig kapasitet: 3
> 1
Hvor mange kommer? 5
For mange! Slipp inn 3
Ledig kapasitet: 0
> 2
Hvor mange går? 4
Ledig kapasitet: 4
> 0
Takk for nå
>>>
'''
def kapasitetVakt(kapasitet):
    ledig_kap = kapasitet

    print(f'\
Noen ankommer - tast 1\n\
Noen går - tast 2\n\
Avslutt - 0\n\
Ledig kapasitet: {ledig_kap}')
    while True:
        i = int(input(':'))

        if i == 1:
            add = int(input('Hvor mange kommer? '))
            if add < ledig_kap:
                ledig_kap -= add                                # trekker fra inpasserende
                print(f'Ledig kapasitet: {ledig_kap}\n')
            else:
                print(f'For mange! Slip in: {ledig_kap}')     
                ledig_kap = 0                                   # (ledig_kap -= ledig_kap) == 0. trekker fra mulig inpaserende
                print(f'Ledig kapasitet: {ledig_kap}\n')

        elif i == 2:
            subt = int(input('Hvor mange går? '))
            ledig_kap += subt                                   # legger til utpasserende slik at ledig kapasitet øker
            print(f'Ledig kapasitet: {ledig_kap}\n')


        elif i == 0:
            print('Takk for nå')
            break

kapasitetVakt(10)