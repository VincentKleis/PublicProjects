emner=[ ('PRO100','Programmering 1',10,[]),
        ('PRO110','Programmering 2',10,['PRO100']),
        ('PRO220','Avansert programmering',10,['PRO110','MAT120']),
        ('MAT120','Driskret Matematikk',10,[]),
        ('MET120','Kvalitativ metode',10,[])
        ]

studenter = {   'Kari':['Geografi',{'PRO100':'A','PRO110':'B','STK100':'C', 'DATA120':'B'}],
                'Anne':['Fysikk',{'MET120':'B','STK100':'C', 'MAT130':'A'}],
                'Nils':['Økonomi',{'PRO100':'B','PRO110':'A', 'DAT130':'C', 'MET120':'F'}]}

# # a)

# def finn_emne(emnekode:str):
#     for i in emner:
#         if emnekode in i:
#             x,y,z,w = i
#             return(y,z,w)

# # test

# print(finn_emne('PRO220'))
# print(finn_emne('MET120'))

# # b)

# def bestått(student:str, emnekode:str)-> bool:
#     studier = studenter[student][1]
#     stå_karakterer = ['A','B','C','D','E']

#     try:
#         if studier[emnekode] in stå_karakterer:
#             return True
#         else:
#             return False
#     except:
#         return False

# # test
# print(bestått('Kari','PRO100'))
# print(bestått('Anne','PRO100'))
# print(bestått('Nils','MET120'))