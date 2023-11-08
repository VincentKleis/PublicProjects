year = int(input('Hvilket år er det? '))

if year % 4 == 0:
    print(f'{year} is a leep year')
elif year % 400 == 0 and year % 100 == 0:
    print(f'{year} is a leep year')
else:
    print(f'{year} is not a leep year')