def tre_små_kinesere(x: str):
    tekst = '''\
tre små kinesere på høybro plass
sto og spilte på en kontrabass
så kom en konstabel, spurte hva var hendt
tre små kinesere på høybro plass'''
    vokaler = ['a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å']
    kineser_list = []
    kineser_list[:0] = tekst
    ny_tekst = [x if i in vokaler else i for i in kineser_list]
    return ''.join(ny_tekst)

# test
print(tre_små_kinesere('i'))