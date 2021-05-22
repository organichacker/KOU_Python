import pandas as pd
import matplotlib.pyplot as plt

Kaynak = pd.read_csv('C:\\Python\\Project\\Deneme\\top50.csv')
bosListe =[]
tur = []
sozluk = {}
Kaynak_Genre = Kaynak['Genre'][:]
Kaynak_Danceability = Kaynak['Danceability'][:]

for i in range(Kaynak.shape[0]):
    a = Kaynak_Genre[i]
    b = Kaynak_Danceability[i]
    if a in tur:
        sozluk[str(a)]['Sayi'] +=1
        sozluk[str(a)]['Dance'] = sozluk[str(a)]['Dance'] + int(b)
        pass
    if not a in tur:
        tur.append(a)
        sozluk[str(a)] = {"Sayi" : 1,"Dance" : b}

for i in sozluk:
    j = int(sozluk[str(i)]['Dance']/sozluk[str(i)]['Sayi'])
    bosListe.append(j)

x = list(sozluk.keys())
y = bosListe
plt.barh(x,y)
plt.show()
