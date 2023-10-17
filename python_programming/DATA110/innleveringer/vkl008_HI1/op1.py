import math

def pi(d=2):
    pi = math.pi
    if d > 15:
        print('For mange desimaler')
    x = round(pi, d)
    return x

#############################
##########TEST###############
print(pi(4))
print(pi(10))
print(pi(50))
print(pi())