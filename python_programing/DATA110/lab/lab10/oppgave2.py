tall = [1,2,3,4]
def alle_kombinasjoner(x:list)-> tuple:
    liste = []
    leng = len(x)
    for i in x:
        count = 0
        while leng > count:
            liste.append((i, tall[count]))
            count += 1
    
    return liste

print(alle_kombinasjoner(tall))