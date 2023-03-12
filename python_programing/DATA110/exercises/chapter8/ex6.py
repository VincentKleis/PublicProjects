user_number_list = []
while True:
    user_number = input('Enter a number: ')
    if user_number == 'done': break
    user_number_list.append(user_number)

print(f'Maximum: {float(max(user_number_list))}')
print(f'Minimum: {float(min(user_number_list))}')
