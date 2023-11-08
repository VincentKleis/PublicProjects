letter = input('input a letter in the a-h range: ')
number = int(input('input whole number between 1-8: '))

odd_num = number % 2 == 1
other_letter = 'aceg'

if odd_num:
    if letter in other_letter:
        print('Black')
    if letter not in other_letter:
        print('White')
if not odd_num:
    if letter in other_letter:
        print('White')
    if letter not in other_letter:
        print('Black')
