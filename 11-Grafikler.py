import pandas as pd
from pandas import DataFrame

data = {'Öğrenci': ['Ali', 'Ayşe', 'Mehmet', 'Ahmet', 'Aylin', 'Mustafa', 'Ebru', 'Can', 'Deniz', 'Gizem',
                    'İbrahim', 'Elif', 'Burak', 'Fatma', 'Emre', 'Ceren', 'Gül', 'Kadir', 'İrem', 'Ozan'],
        'Ders': ['Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya',
                 'Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya',
                 'Matematik', 'Fizik'],
        'Not': [90, 85, 95, 75, 80, 92, 87, 88, 93, 82, 79, 91, 86, 89, 78, 83, 94,81,84,90]}
df: DataFrame = pd.DataFrame(data)
print(df.head())
#not sutun ortalaması
mean =df["Not"].mean
print("ortalama",mean)
#not sutun medyanı
median = df["Not"].median()
print("median",median)
#not sutun modu
mode = df["Not"].mode()
print("mode",mode)
#not sutun standart sapması
std = df["Not"].std()
print("std",std)
#not sutun min değeri
min = df["Not"].min()
print("min",min)
#not sutun max değeri
max = df["Not"].max()
print("max",max)
#not sutun toplam
sum = df["Not"].sum()
print("sum",sum)
#not sutun varyansı
variance = df["Not"].var()
print("variance",variance)
#not sutunda kaç adet değer var
count = df["Not"].count()
print("count",count)
#not sutunun yüzdelik dilimleri
quartile = df["Not"].quantile([0.25,0.50,0.75])
print("yüzdelik dilimker")
print(quartile)
#not sutun koralasyonu
#correlation = df["Not"].corr()
#print("correlation",correlation)
#correlation=df["not"]

ders_gruppe = df.groupby("Ders")
ortalama =ders_gruppe["Not"].mean
print("derlere göre ortalama")
print(ortalama)

toplam_notlar=ders_gruppe["Not"].min()
print("derlere göre min")
print(toplam_notlar)

en_yüksek = ders_gruppe["Not"].max
print("derlere göre max")
print(en_yüksek)

sıralı_veri=df.sort_values(by="Not",ascending=False)
print("notlara gçre sıralı veri")
print(sıralı_veri)

yükseknotlar =df[df["Not"] >85 ]
print("not 85 den yüksekse")
print(yükseknotlar)

matematik=df[df["Ders"]=="Matematik"]
print(matematik)


df1 = pd.DataFrame({'Öğrenci': ['Ali', 'Ayşe', 'Mehmet', 'Ahmet'],
                    'Ders': ['Matematik', 'Fizik', 'Kimya', 'Matematik'],
                    'Not': [90, 85, 95, 75]})

# İkinci veri çerçevesi
df2 = pd.DataFrame({'Öğrenci': ['Ali', 'Ayşe', 'Mehmet', 'Ahmet'],
                    'Yaş': [18, 17, 19, 16],
                    'Cinsiyet': ['Erkek', 'Kadın', 'Erkek','Erkek']})
birleştir=pd.merge(df1,df2 , on="Öğrenci")

matematik = birleştir[birleştir["Ders"]=="Matematik"]
print("Matematik dersi alan öğrenciler")
print(matematik)

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[6,7,8,9,10]
df =pd.DataFrame({"x":x,"y":y})
df.plot(x="x",y="y", kind="line")
plt.title("cizgi grafiği")
plt.xlabel("x değeri")
plt.ylabel("y değeri")
plt.show()



categories =["A","B","C","D","E"]
values=[1,2,3,4,5,]
df =pd.DataFrame({"category":categories,"values":values})
df.plot(x="category",y="values",kind="bar")
plt.show()



data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8, 8]
df = pd.DataFrame({'Data': data})
df.plot.hist()
plt.title('Histogram Grafiği')
plt.xlabel('Data')
plt.ylabel('Frequency')
plt.show()




x=[1,2,3,4,5]
y=[6,7,8,9,10]
df =pd.DataFrame({"x":x,"y":y})
#df.plot(x="x",y="y",kind="scatter",color="red")
df.plot.scatter(x="x",y="y")
plt.show()

data = [1,2,3,4,5,6,7,8,9,10]
df = pd.DataFrame({"data": data})
df.plot.box()
plt.title('Box')
plt.ylabel('Data')
plt.show()




data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8, 8]
df = pd.DataFrame({'Data': data})
# Histogram grafiği oluşturma
df.plot.hist()
plt.title('Histogram Grafiği')
plt.xlabel('Data')
plt.ylabel('Frequency')
plt.show()




data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
df = pd.DataFrame({'Data': data})
df.plot.box()
plt.title('Kutu Grafiği')
plt.ylabel('Data')
plt.show()
import seaborn as sns

data = [1,2,3,4,5,6,7,8,9,10]
df = pd.DataFrame({"data":data})
sns.kdeplot(df["data"].to_numpy())

plt.title('yoğunluk garfiği')
plt.xlabel("Değer")
plt.ylabel("yoğunluk")
plt.show()


#veri oluşturma
sizes=[30,25,20,15,10]
labels=['A','B','C','D','E']
#pasta grafiği oluşturma
plt.pie(sizes,labels=labels)
#Grafiği özelleştirme
plt.title('Pasta Grafiği')
#Grafiği gösterme
plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax=fig.add_subplot(111,projection='3d')
plt.show()



soa=np.array([[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]])
Z,Y,Z,U,V ,W=zip(*soa)
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

ax.set_xlim([-4,4])
ax.set_ylim([-4,4])
ax.set_zlim([0,4])

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.xaxis.label.set_color('r')
ax.yaxis.label.set_color('g')
ax.zaxis.label.set_color('b')
plt.show()

#veri seti ve 3 boyutlu kartezyen yapı
soa=np.array([[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]])
Z,Y,Z,U,V,W=zip(*soa)
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
# boyutlara değer
ax.set_xlim([-4,4])
ax.set_ylim([-4,4])
ax.set_zlim([0,4])

# boyutlara isim atama
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# boyutlara renk atama
ax.xaxis.label.set_color('r')
ax.yaxis.label.set_color('g')
ax.zaxis.label.set_color('b')
colors=['r','g','b',"r","r","g","g","b","b"]
quivers=ax.quiver(Z,Y,Z,U,V,W, color =colors)
plt.show()
