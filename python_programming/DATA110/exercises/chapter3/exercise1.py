houre = input ('Houres a week: ')
rate = input ('Rate of pay: ')
if int(houre) > 40:
    extra_houres = int(houre) - 40
    overtime = extra_houres * 1.5 * float(rate) #if houre surpasses 40 add overtime
    gros_pay = (int(houre) - extra_houres) * float(rate) + overtime

else:
    gros_pay = int(houre) * float(rate)

print ( 'Pay:', gros_pay )
