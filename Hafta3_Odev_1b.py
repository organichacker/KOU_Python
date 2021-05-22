import pandas as pd

tur = []
sozluk = {}
Kaynak = pd.read_csv('C:\\Python\\Project\\Deneme\\top50.csv')

Kaynak_Genre = Kaynak['Genre'][:]


for i in range(Kaynak.shape[0]):
    a = Kaynak_Genre[i]
    if a in tur:
        sozluk[str(a)] +=1
        pass
    if not a in tur:
        tur.append(a)
        sozluk[str(a)] = 1

print(sozluk)
