import matplotlib.pyplot as plt
import pandas as pd

Kaynak = pd.read_csv('C:\\Python\\Project\\Deneme\\top50.csv')

tur = []
        
for i in range(Kaynak.shape[0]):
    a = Kaynak.Genre[i]
    if a in tur:
        pass
    if not a in tur:
        tur.append(a)
        
print(tur)
