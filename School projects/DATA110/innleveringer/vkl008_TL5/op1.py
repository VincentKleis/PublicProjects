def antall_vokaler(x):
    n = 0
    vokaler = ['a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å']
    for i in x:
        if i in vokaler:
            n += 1
    return n

# test
print(antall_vokaler('Tre små kinesere på Høybro plass'))