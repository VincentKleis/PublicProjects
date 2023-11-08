import pandas as pd

excel_data = pd.read_excel("98014750339_2023_05_01-2023_09_24.xlsx")

data = pd.DataFrame(excel_data)

bank_data = data.loc[list(range(2,142))]

bank_data.rename({"Unnamed: 0":"BOKFØRINGSDATO", "Unnamed: 1":"RENTEDATO",	
        "Unnamed: 2":"ARKIVREFERANSE",	"Unnamed: 3":"MOTKONTO", "Unnamed: 4": "TYPE",
        "UTGÅENDE SALDO 24.09.2023":"TEKST", "Unnamed: 6": "UT FRA KONTO", "719.99":"INN PÅ KONTO"})

print(bank_data)