fahrenheit = int(input('Farenheit: '))                  #fyll in farenheight
celsius = (fahrenheit - 32) * (5/9)
print('%.2f' % fahrenheit,'grader Fahrenheit tillsvarer','%.2f' % celsius,'grader Celsius')
fahrenheit = celsius * 1.8 + 32
print('%.2f' % celsius,'grader Celsius tillsvarer','%.2f' % fahrenheit,'grader Fahrenheit')
