def palindrom(x:str, ingorer_mellomrom: bool = False) -> bool:
    # Pre-processing
    x = x.lower()

    processed_string = ''
    for letter in x:
        if letter in f"{'' if ingorer_mellomrom else ' '}abcdefghijklmnopqrstuvwxyzæøå":
             processed_string += letter

    center = len(x) // 2

    # Test
    pal_test1 = x[:center]
    pal_test2 = x[::-1][:center]

    return pal_test1 == pal_test2

print(palindrom('pip'))

print(palindrom('regninger'))

print(palindrom('regning'))

print(palindrom('A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!'))