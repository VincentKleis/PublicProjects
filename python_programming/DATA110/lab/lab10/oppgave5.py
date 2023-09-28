# with open('lab\lab10\Temp fil.txt', 'r', encoding='utf8') as fhand:
#     fil = fhand.readlines()

# def temp_data(data: list)-> list:
#     liste = []
#     for i in data:
#         i = i.split(' ')
#         liste.append( (i[0], i[1], round(float(i[2].rstrip('\n')))) )
    
#     return liste

# def sett_temperatur():
#     fil[-1] += '\n'
#     sted = input('Sted: ')
#     dag = input('Dag: ')
#     temperatur = input('Temperatur: ')
#     fil.append(f'{sted} {dag} {temperatur}')
    
# def snit_sted() -> list:
#     info = temp_data(fil)
#     sted_temp = {}

#     for i in info:
#         snit_i = 0
#         if i not in sted_temp:
#             count= 0
#             for x in info:
#                 if x[0] == i[0]:
#                     snit_i += x[2]
#                     count += 1
#             snit_i = round(snit_i/count, 2)
#             sted_temp[i[0]] = snit_i

#     output = [f'{i} {sted_temp[i]}' for i in sted_temp]

#     return output

# def ny_fil():
#     with open('lab\lab10\ Ny temp fil.txt', 'w', encoding='utf8') as fhand:
#         fhand.writelines(fil)



# b)
with open('lab\lab10\Temp fil.txt', 'r', encoding='utf8') as fhand:
    fil = fhand.readlines()

def temp_data(data: list)-> list:
    ordlist = {}
    for i in data:
        i = i.split(' ')
        ordlist[ (i[0], i[1]) ] = float(i[2].rstrip('\n'))
    
    return ordlist

def sett_temperatur():
    fil[-1] += '\n'
    sted = input('Sted: ')
    dag = input('Dag: ')
    temperatur = input('Temperatur: ')
    fil.append(f'{sted} {dag} {temperatur}')
    
def snit_sted() -> list:
    info = temp_data(fil)
    sted_temp = {}

    for i in info:
        snit_i = 0
        if i not in sted_temp:
            count= 0
            for x in info:
                if x[0] == i[0]:
                    snit_i += x[2]
                    count += 1
            snit_i = round(snit_i/count, 2)
            sted_temp[i[0]] = snit_i

    output = [f'{i} {sted_temp[i]}' for i in sted_temp]

    return output

def ny_fil():
    with open('lab\lab10\ Ny temp fil.txt', 'w', encoding='utf8') as fhand:
        fhand.writelines(fil)

print(temp_data(fil))