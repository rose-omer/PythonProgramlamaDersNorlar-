'''  grafik sorusu gelecek
     algoritma soruları

'''



import pandas as pd
import matplotlib.pyplot as plt
# Zaman serisi veri setini oluşturalım
data = {'Tarih': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04',
'2021-01-05'],
'Değer': [10, 15, 12, 18, 20]}
df = pd.DataFrame(data)


# Tarih sütununu zaman formatına dönüştürelim
df['Tarih'] = pd.to_datetime(df['Tarih'])
# Tarih sütununu indeks olarak ayarlayalım
df.set_index('Tarih', inplace=True)
# Zaman serisi veriyi görselleştirelim
df.plot()
plt.xlabel('Tarih')
plt.ylabel('Değer')
plt.title('Zaman Serisi Veri')
plt.show()


# Veri setini oluşturalım
data = {'Şehir': ['İstanbul', 'İstanbul', 'İstanbul', 'Ankara', 'Ankara',
'Ankara'],
'Bölge': ['Avrupa', 'Avrupa', 'Anadolu', 'Anadolu', 'Avrupa',
'Anadolu'],
'Mevsim': ['Yaz', 'Kış', 'İlkbahar', 'Kış', 'Yaz', 'İlkbahar'],
'Sıcaklık': [30, 10, 20, 5, 25, 15]}
df = pd.DataFrame(data)
# Çoklu indeksleme için sütunları indeks olarak ayarlayalım
df.set_index(['Şehir', 'Bölge', 'Mevsim'], inplace=True)
# Çok seviyeli veri çerçevesini görüntüleyelim
print(df)


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Veri kümesini oluşturma
veri = {'Grup': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
        'Değer': [25, 32, 42, 18, 28, 36,55,60,48]}
df = pd.DataFrame(veri)

sns.boxplot(data=df, x='Grup', y='Değer')
plt.xlabel("Grup")
plt.ylabel("değer")
plt.title("değer dağılımı")
plt.show()



#veri kümesini oluşturma
veri = {'Kategori': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
        'Özellik 1': [3, 4, 2, 1, 5, 2, 3, 2, 4],
        'Özellik 2': [1, 2, 3, 4, 5, 1, 2, 3, 4],
        'Özellik 3': [4, 3, 2, 1,2,4,3,2,1]}
df=pd.DataFrame(veri)

#Kategorik sütunu sayısal değerlere dönüştürme
df['Kategori']=pd.Categorical(df['Kategori'])
df['Kategori']=df['Kategori'].cat.codes

#Korelasyon matrisini oluşturma
korelasyon = df.corr()

#Isı haritasını oluşturma
sns.heatmap(korelasyon, annot=True, cmap='RdYlBu')

#Başlık ekleme
plt.title('Özellik Korelasyonları')

#Grafiği görüntüleme
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
'''
# Veri kümesini oluşturma
veri = {'Reklam_Harcamalari': [100, 200, 300, 400, 500],
        'Satislar': [1500, 2200, 3200,4200,5000]}


df=pd.DataFrame(veri)
x =df[["reklam harcamaları"]]
y = df[["satislar"]]

model = LinearRegression()
model.fit(x,y)

plt.scatter(x, y, color='blue', label='veri noktaları')
plt.plot(x, model.predict(x), color='red' ,label='regresyon doğrusu')
plt.xlabel('reklam')
plt.ylabel('satislar')

plt.title("reklam harcamalarına ve satışlarına arasındaki ilişki ")
plt.legend()
plt.show()
'''


# Veri kümesini oluşturma
veri = {'X': [1, 2, 3, 4, 5],
        'Y': [2, 4, 5, 4, 5]}
df=pd.DataFrame(veri)

#Seaborn stilini ayarlama
sns.set()

#çizgi grafiği oluşturma
sns.lineplot(data=df,x='X', y='Y')

#eksen grafikleri ve başlık ekleme
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Çizgi Grafiği')

#grafiği görüntüleme
plt.show()



#sns ayarlama
sns.set_style("whitegrid")

#nokta grafiğini oluşturma
sns.scatterplot(data=df,x='X',y='Y')

#Eksen etiketleri ve başlık ekleme
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Nokta Grafiği')

#grafiği görüntüleme
plt.show()
'''

veri = {"Katagori":["A", "B", "C", "D","E"],
        'değer': [10, 20, 30, 40, 50]}

df=pd.DataFrame(veri)
renkler=sns.color_palette("bright")
sns.barplot(data=df,x='Katagori',y ="değer", palette=renkler)
plt.xlabel('Katagori')
plt.ylabel('değer')
plt.title('cubuk Grafiği')

plt.show()
'''
veri={"x": [1,2,3,4,5,],
      "y": [10,20,30,40,50]}
df=pd.DataFrame(veri)
sns.set_style("darkgrid")
sns.set(rc={"axes.facecolor":"lightgrey"})
sns.lineplot(data=df,x='x',y="y",linestyle="dashed")
plt.xlabel('x')
plt.ylabel('y')
plt.title('cizgi grafiği')

plt.show()




'''
        veri okutacak 
        grafikler
        son slayta kadar her şey sorumlyuz
'''