def oversett(ord: str, text_file: str) -> str:

    oversetter = []

    with open(text_file, 'r') as ordliste:
        for line in ordliste:
            if ',' in line:
                line_list = line.split(',')
            elif '.' in line:
                line_list = line.split('.')

            oversetter.append(f'{line_list[0].strip()}: {line_list[1].strip()}')

    count = 0

    for i in oversetter:
        if i[:len(ord)] == ord:
            h_ = i[:i.index(':')]
            _v = i[i.index(':')+2:]
            oversettelse = f'{h_} = {_v}'
            print(oversettelse)
            count += 1
    else:
        if count == 0: print(f'{ord} er ikke i ordlisten')
        

print("Oppgi søkeord (avslutt med 'slutt')")
while True:
    ord = input('søkeord: ')

    if ord == 'slutt':
        break

    oversett(ord, 'ordliste.txt')