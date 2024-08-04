import  numpy as np
dizi =np.array([1,2,3,4,5,6,7,8,9])
print(dizi)
print(type (dizi))
print(type (dizi.dtype))
print()
dizi=np.array([[1,2,3],[4,5,6]])
print(dizi)
print()
dizi=np.array([[0,1,2,3],[4,4,5,6],[7,8,9,10]])
print(dizi)

print(dizi.ndim)
print(dizi.shape)
print(dizi.reshape(4,3))


dizi =np.arange(30)
print(dizi.reshape(6,5))

dizi =np.arange(0,30,3)
print(dizi)

dizi =np.random.random(4)
print(dizi)

dizi = np.random.randint(20 ,size=4)
print(dizi)

# sınavda random.random ve rand om.randint arasında fark ile ilgili soru gelebilir

dizi =np.random.random((2,4))
print(dizi)





dizi =np.arange(8)
dizi=dizi.reshape(4,2)
print(dizi)
dizi2=dizi[0:2]
print(dizi2)


dizi =np.arange(8)
dizi =dizi.reshape(4,2)
print(dizi)
dizi2 =dizi[:,0]
print(dizi2)



dizi =np.zeros((5,3))
print(dizi)

dizi =np.ones((2,3,4))
print(dizi)
dizi =np.ones((2,4))*5
print(dizi)

veri =np.full((2,3),8)
print(veri)
print()

dizi=np.eye(3)
print(dizi)


matris1 =np.array([[1,2,3],[4,5,6]])
matris2 =np.array([[7,8,9], [10,11,12]])
birleştirme =np.concatenate((matris1,matris2))
print(birleştirme)

birleştirme =np.concatenate((matris1,matris2) ,axis=1)
print(birleştirme)

dizi=np.array([[1,2,3],[4,5,6]])
print(dizi.max())
print(dizi.min())
print(dizi.sum())
print(dizi.sum(axis=1))
print(dizi.sum(axis=0))
print(dizi.mean())
print(dizi.var())
print(dizi.std())

dizi=np.array([[1,2,3],[4,5,6]])
dizi2=np.array([[7,8,9], [10,11,12]])
sonuç=dizi+dizi2
print(sonuç)
print()
sonuç =dizi-dizi2
print(sonuç)
print()
sonuç=dizi*dizi2
print(sonuç)

print()
sonuç = dizi/dizi2
print(sonuç)

sonuç=dizi%dizi2
print(sonuç)
print()
print()
sonuç =dizi2+10
print(dizi2)


dizi =np.array([[1,2,3],[4,5,6]])
sonuç =np.sin(dizi)
print(sonuç)

matris1= np.array([[1,2],[4,5]])
matris2= np.array([[7,8],[10,11]])
sonuç= np.dot(matris1,matris2)
print(sonuç)

matris1 = np.array([[1,2,3],[4,5,6]])
transpoz= np.transpose(matris1)
print(transpoz)

dizi= np.array([[1,2,3],[4,5,6],[7,8,9]])
kontrol =dizi<4
print(kontrol)

kosulDeğerleri =dizi[dizi <4 ]
print(kosulDeğerleri)


dizi= np.array([1, 2, 3, 4, 5])
np.save("deneme",dizi)
yeni_dizi= np.load("deneme.npy")
print(yeni_dizi)

'''
dosyayolu="ornek.csv"
veri=np.genfromtxt(dosyayolu,delimiter=",")
print(veri)'''

# Örnek bir dizi oluşturalım.
dizi = np.array([1, 2, 3, 4, 5])
# Diziyi "deneme.npy" adlı bir dosyaya kaydedelim
np.save("deneme.npy", dizi)
# "deneme.npy" dosyasındaki verileri yeni_dizi adlı değişkene yükleyelim.
yeni_dizi = np.load("deneme.npy")
# Yüklenen diziyi ekrana yazdıralım
print(yeni_dizi)