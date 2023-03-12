name = 'Mitt navn er vincent'
name_vincent = name.find('vi')
name_intro = name[0:name_vincent-1]
print(name.capitalize())
name_german = 'Vinßent'
print(name_intro, name_german.casefold())
casef_german = name_german.casefold()
print(name_intro,casef_german.replace('ss','c'))
print(name.lstrip('Mit naerz'))
print(name.removeprefix('Mitt navn er '))
