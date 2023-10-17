sentence = input('Gi meg en setning: ')
index = 0
while index > (len(sentence) * (-1)):
    print(sentence[index-1])  #printer siste bokstav i setningen og går bakover til den når 0
    index = index - 1
