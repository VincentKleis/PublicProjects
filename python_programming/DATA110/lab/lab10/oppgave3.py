dager=[(1,'man'),(2,'tir'),(3,'ons'),(4,'tor'),(5,'fre'),\
        (6,'lør'),(7,'søn')]
temperaturer=[('man',11),('tir',9),('ons',7),('tor',12),\
                ('fre',11),('lør',9),('søn',8)]

def koble(tup: list, tup2:list) -> list:
    list = []
    count = 0
    while len(tup) > count:
        v, x = tup[count]
        count2 = 0
        while len(tup2) > count2:
            y, z = tup2[count2]
            if y == x:
                list.append( (v,z) )
            count2 += 1
        count += 1

    return list

print(koble(dager, temperaturer))
