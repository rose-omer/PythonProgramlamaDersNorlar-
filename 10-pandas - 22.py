import pandas as pd

data = {
    'Öğrenci': ['Ali', 'Ayşe', 'Mehmet', 'Ahmet', 'Aylin', 'Mustafa', 'Ebru',
                'Can', 'Deniz', 'Gizem',
                'İbrahim', 'Elif', 'Burak', 'Fatma', 'Emre', 'Ceren', 'Gül',
                'Kadir', 'İrem', 'Ozan'],
    'Ders': ['Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya',
             'Matematik', 'Fizik', 'Kimya',
             'Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya',
             'Matematik', 'Fizik', 'Kimya',
             'Matematik', 'Fizik'],
    'Not': [90, 85, 95, 75, 80, 92, 87, 88, 93, 82, 79, 91, 86, 89, 78, 83,
            94, 81, 84, 90]
}

df = pd.DataFrame(data)
# Veri çerçevesinin ilk 5 satırını gösterme
print(df.head())
# Not sütununun ortalaması
mean = df['Not'].mean()
print("Ortalama:", mean)
# Not sütununun medyanı
median = df['Not'].median()
print("Medyan:", median)
# Not sütununun modu
mode = df['Not'].mode()
print("Mod:", mode)
# Not sütununun toplamı
total = df['Not'].sum()
print("Toplam:", total)
# Not sütununun en küçük değeri
min_value = df['Not'].min()
print("En Küçük Değer:", min_value)
# Not sütununun en büyük değeri
max_value = df['Not'].max()
print("En Büyük Değer:", max_value)
# Not sütununun standart sapması
std = df['Not'].std()
print("Standart Sapma:", std)
# Not sütununun varyansı
var = df['Not'].var()
print("Varyans:", var)
# Not sütununda kaç adet değer var
count = df['Not'].count()
print("Toplam Sayı:", count)
# Not sütununun yüzdelik dilimleri (25%, 50%, 75%)
quantiles = df['Not'].quantile([0.25, 0.50, 0.75])
print("Yüzdelik Dilimler:")
print(quantiles)
# Not sütununun korelasyon matrisi
correlation = df['Not'].corr(df['Not'])
print("Korelasyon:", correlation)

df = pd.DataFrame(data)

# Derslere göre gruplama yapma ve ortalamaları hesaplama
ders_gruplari = df.groupby('Ders')
ortalama = ders_gruplari['Not'].mean()
print("Derslere Göre Ortalamalar:")
print(ortalama)


# Derslere göre gruplama yapma ve en düşük notları hesaplama
toplam_notlar = ders_gruplari['Not'].min()
print("Derslere En Düşük Notlar:")
print(toplam_notlar)


# Derslere göre gruplama yapma ve en yüksek notları hesaplama
en_yuksek_notlar = ders_gruplari['Not'].max()
print("Derslere Göre En Yüksek Notlar:")
print(en_yuksek_notlar)


# Not sütununa göre büyükten küçüğe sıralama
sirali_veri = df.sort_values(by='Not', ascending=False)
print("Notlara Göre Sıralı Veri:")
print(sirali_veri)


# Matematik dersine ait verileri filtreleme
matematik_verileri = df[df['Ders'] == 'Matematik']
print("Matematik Dersine Ait Veriler:")
print(matematik_verileri)


# Notu 85'ten büyük olan öğrencileri filtreleme
yüksek_notlar = df[df['Not'] > 85]
print("85'ten Büyük Nota Sahip Öğrenciler:")
print(yüksek_notlar)


# İlk veri çerçevesi
df1 = pd.DataFrame({'Öğrenci': ['Ali', 'Ayşe', 'Mehmet', 'Ahmet'],
                    'Ders': ['Matematik', 'Fizik', 'Kimya', 'Matematik'],
                    'Not': [90, 85, 95, 75]})
# İkinci veri çerçevesi
df2 = pd.DataFrame({'Öğrenci': ['Ali', 'Ayşe', 'Mehmet', 'Ahmet'],
                    'Yaş': [18, 17, 19, 16],
                    'Cinsiyet': ['Erkek', 'Kadın', 'Erkek', 'Erkek']})
# Veri çerçevelerini birleştirme
birlesik_df = pd.merge(df1, df2, on='Öğrenci')
# Örneğin, Matematik dersini alan öğrencileri filtreleme
matematik_dersi_alanlar = birlesik_df[birlesik_df['Ders'] == 'Matematik']
print("Matematik Dersi Alan Öğrenciler:")
print(matematik_dersi_alanlar)

import matplotlib.pyplot as plt

# Veri oluşturma
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 9]
# Veri çerçevesini oluşturma
df = pd.DataFrame({'x': x, 'y': y})
# Çizgi grafiği oluşturma
df.plot(x='x', y='y', kind='line')
# Grafik özelliklerini ayarlama
plt.title('Çizgi Grafiği')
plt.xlabel('x değerleri')
plt.ylabel('y değerleri')
# Grafiği gösterme
plt.show()

categories = ['A', 'B', 'C', 'D']
values = [20, 10, 15, 25]
# Veri çerçevesini oluşturma
df = pd.DataFrame({'Category': categories, 'Value': values})
# Sütun grafiği oluşturma
df.plot(x='Category', y='Value', kind='bar')
# Grafik özelliklerini ayarlama
plt.title('Sütun Grafiği')
plt.xlabel('Category')
plt.ylabel('Value')
# Grafiği gösterme
plt.show()

# Veri oluşturma
data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8, 8]
# Veri çerçevesini oluşturma
df = pd.DataFrame({'Data': data})
# Histogram grafiği oluşturma
df.plot.hist()
# Grafik özelliklerini ayarlama
plt.title('Histogram Grafiği')
plt.xlabel('Data')
plt.ylabel('Frequency')
# Grafiği gösterme
plt.show()

# Veri oluşturma
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 9]
# Veri çerçevesini oluşturma
df = pd.DataFrame({'x': x, 'y': y})
# Nokta grafiği oluşturma
df.plot.scatter(x='x', y='y')
# Grafik özelliklerini ayarlama
plt.title('Nokta Grafiği')
plt.xlabel('x')
plt.ylabel('y')
# Grafiği gösterme
plt.show()

# Veri oluşturma
data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
# Veri çerçevesini oluşturma
df = pd.DataFrame({'Data': data})
# Kutu grafiği oluşturma
df.plot.box()
# Grafik özelliklerini ayarlama
plt.title('Kutu Grafiği')
plt.ylabel('Data')
# Grafiği gösterme
plt.show()

sizes = [30, 25, 20, 15, 10]  # Dilim boyutları
labels = ['A', 'B', 'C', 'D', 'E']  # Dilim etiketleri
# Pasta grafiği oluşturma
plt.pie(sizes, labels=labels)
# Grafik özelliklerini ayarlama
plt.title('Pasta Grafiği')
# Grafiği gösterme
plt.show()

# Veri oluşturma
years = [2010, 2011, 2012, 2013, 2014]
data1 = [10, 15, 12, 8, 20]
data2 = [5, 8, 6, 10, 12]
# Veri çerçevesini oluşturma
df = pd.DataFrame({'Year': years, 'Data1': data1, 'Data2': data2})
# Alan grafiği oluşturma
df.plot.area(x='Year')
# Grafik özelliklerini ayarlama
plt.title('Alan Grafiği')
plt.xlabel('Year')
plt.ylabel('Value')
# Grafiği gösterme
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
# Veri oluşturma
data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
# Veri çerçevesini oluşturma
df = pd.DataFrame({'Data': data})
# Yoğunluk grafiği oluşturma
sns.kdeplot(data=df['Data'].to_numpy())
# Grafik özelliklerini ayarlama
plt.title('Yoğunluk Grafiği')
plt.xlabel('Değer')
plt.ylabel('Yoğunluk')
# Grafiği gösterme
plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.show()

soa = np.array([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0,
                                                         1]])
Z, Y, Z, U, V, W = zip(*soa)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-4, 4])
ax.set_ylim([-4, 4])
ax.set_zlim([0, 4])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.xaxis.label.set_color('r')
ax.yaxis.label.set_color('g')
ax.zaxis.label.set_color('b')

soa = np.array([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]])
Z, Y, Z, U, V, W = zip(*soa)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-4, 4])
ax.set_ylim([-4, 4])
ax.set_zlim([0, 4])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.xaxis.label.set_color('r')
ax.yaxis.label.set_color('g')
ax.zaxis.label.set_color('b')
ax.xaxis.line.set_color('r')
ax.yaxis.line.set_color('g')
ax.zaxis.line.set_color('b')
colors = ['r', 'g', 'b', 'r', 'r', 'g', 'g', 'b', 'b']
quivers = ax.quiver(Z, Y, Z, U, V, W, color=colors)
plt.show()

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
