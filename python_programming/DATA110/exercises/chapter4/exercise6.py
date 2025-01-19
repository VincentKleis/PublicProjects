houre = input('Enter Houres: ')
try:
    int(houre)
    rate = input ('Rate of pay: ')
    float(rate)
except:
    print('Enter numerical value ')
    quit()

time_and_a_half = int(houre) - 40
def computepay():
    overtime = time_and_a_half * 1.5 * float(rate)
    pay = overtime + (int(houre) - time_and_a_half) * float(rate)
    return pay

print(computepay())
