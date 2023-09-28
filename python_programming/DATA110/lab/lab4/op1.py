# del a)
alder = int(input('hvor gammel er du? '))
def myndig(alder : int):
    if alder < 18:
        print('ikke myndig...')
    else:
        print('myndig!')
myndig(alder)
# del b)
alder = int(input('hvor gammel er du? '))
def myndig(alder):
    """[summary]

    Args:
        alder ([type]): [description]

    Returns:
        [type]: [description]
    """
    if alder < 18:
        return 'ikke myndig...'
    if alder > 17:
        return 'myndig!'

print(f'Du er {myndig(alder)}')