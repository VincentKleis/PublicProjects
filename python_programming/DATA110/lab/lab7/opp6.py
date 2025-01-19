def skriv_stor_små(x:str) -> str:
    ord = x.split()
    nye_ord = [x.upper() if ord.index(x)%2 == 0 else x.lower() for x in ord]
    return ' '.join(nye_ord)

# test
print(skriv_stor_små('Tre små kinesere på Høybro plass'))