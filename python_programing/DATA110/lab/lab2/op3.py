import random
rand_num = random.randint(0, 100)
x = 0
string_q = ''
while x < rand_num:
    string_q = string_q + '?'
    x = x + 1

print(string_q)
guess = int(input("Guess the number of '?':"))

if guess < rand_num:
    print('Wrong Guess')
else:
    print('Correct!')
