# 3.
# Skriv om følgende program slik at den ikke har nestede if-setninger.
# x=int(input('tall:'))
# if x>5 :
#     if x<10 :
#        print('6,7,8 eller 9')
#     if x>=10:
#        print('minst 10')
# if x<=5 :
#    print('max 5')

x = int(input('tall:'))
if 5 < x < 10:
    print('6,7,8 eller 9')
elif 5 < x >= 10:
    print('minst 10')
elif x < 5:
    print('max 5')
