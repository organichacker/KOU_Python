import pandas as pd
Kaynak = pd.read_csv('C:\\Python\\Project\\Deneme\\top50.csv',usecols=['Unnamed: 0','Track.Name','Genre','Danceability'])

Kaynak_Genre = Kaynak['Genre'][:]

import matplotlib.pyplot as plt
y = Kaynak['Danceability'][:]
x = Kaynak['Unnamed: 0'][:]

plt.barh(x, y, height = 0.1)
plt.show()
