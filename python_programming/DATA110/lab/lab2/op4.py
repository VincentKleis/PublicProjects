import math
tall_1 = input('1.tall: ')
tall_2 = input('2.tall: ')
tall_12 = int(tall_1+tall_2)
tall_21 = int(tall_2+tall_1)
print(f'kvatroten av {tall_12} * {tall_21} = {math.sqrt(tall_12*tall_21):.2f}')
