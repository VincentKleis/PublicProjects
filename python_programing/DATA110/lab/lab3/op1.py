fart = int(input('Hva er din fart? '))
if fart > 50:
    bot = 1000 + ((fart - 50)*100)
    print(f'din bot: {bot}kr')
else:
    print('gratulerer! du holdt deg under fartsgrensa!')
