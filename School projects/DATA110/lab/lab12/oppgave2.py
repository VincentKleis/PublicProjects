
def tre_små_musikanter(x= None):
    vokaler = ['a', 'e', 'i', 'o', 'u', 'æ', 'ø', 'å']
    text = """tre små Musikanter på høybro plass
sto og spilte på en kontrabass
så kom en konstabel, spurte hva var hendt
tre små Musikanter på høybro plass"""

    def bytt_vokal(y):
        vokaler = ['a', 'e', 'i', 'o', 'u', 'æ', 'ø', 'å']

        if y in vokaler:
            return x
        else:
            return y



    if x == None:
        print(text)
    else:
        r = [i for i in map(bytt_vokal, text)]
        result = ''
        for i in r:
            result += i

        print(result)
        
tre_små_musikanter('u')
