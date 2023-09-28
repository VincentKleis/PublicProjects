fahrenheit = int(input('Farenheit: '))                   
celsius = (fahrenheit - 32) * 5/9
celsius_symbol = u"\N{degree celsius}"
farenheight_symbol = u"\N{degree fahrenheit}"
print('%.2f' % fahrenheit, farenheight_symbol,' = ','%.2f' % celsius, celsius_symbol, sep='' )
fahrenheit = celsius * 1.8 + 32
print('%.2f' % celsius, celsius_symbol,' = ','%.2f' % fahrenheit, celsius_symbol, sep='')
