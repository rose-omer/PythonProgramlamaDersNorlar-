'''
isim =input("isim ver bilader")
yaş =int(input("yaş kaç moruk"))
eğitim =input("Eğitim kariyeri")

if(yaş >= 18) and (eğitim == "lise" ) or (eğitim=="üni"):
    print(isim +" ehliyet alabilir")
else:
    print(isim+"sana ehliyet verememmm")

vize =int(input("Vize notu"))
final =int(input("Final notu"))
sözlü =int(input("Sözlü "))

ortalama =vize+final+sözlü/3
if(ortalama<24):
    print(0)
elif(44>ortalama>25):
    print(1)
elif(54>ortalama>44):
    print(2)
elif(69>ortalama>55):
    print(3)
elif(84>ortalama>70):
    print(4)
else:
    print(5)







import  datetime
year = int(input("yıl"))
month = int(input("ay"))
day = int(input("gün"))
trafiiğeCıkıs=datetime.datetime(year,month,day)
şimdi =datetime.datetime.now()
fark =şimdi-trafiiğeCıkıs
days =fark.days

if days<=365:
    print("1. seervis aralığı")
elif 365<days<=365*2:
    print("2. seervis aralığı")
elif 365*2<days<=365*3:
    print("3. seervis aralığı")
elif 365*3<days<=365*4:
    print("4. seervis")




sayı =int(input("sayı gir"))
if sayı>0:
    if sayı %2==0:
        print( "cift")
    else:
        print("tek")
else:
    print("sayı negatif olmasın ")





sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
sayi3 = float(input("Üçüncü sayıyı girin: "))
if sayi1 >= sayi2 and sayi1 >= sayi3:
    en_buyuk = sayi1
elif sayi2 >= sayi1 and sayi2 >= sayi3:
    en_buyuk = sayi2
else:
    en_buyuk = sayi3
if sayi1 <= sayi2 and sayi1 <= sayi3:
    en_kucuk = sayi1
elif sayi2 <= sayi1 and sayi2 <= sayi3:
    en_kucuk = sayi2
else:
    en_kucuk = sayi3
ortanca = (sayi1 + sayi2 + sayi3) - (en_buyuk + en_kucuk)
print("Büyükten küçüğe sıralanmış hali:", en_buyuk, ">", ortanca, ">", en_kucuk)







vize =int(input("Vize notu"))
vize2 = int(input("Vize2 notu "))
final =int(input("Final notu"))
ortvize =vize+vize2

ortalama=  ortvize*6/10 + final*4/10
if ortalama > 50:
    if final <50:
        print("kaldı")
    else:
        print("gecti")
elif final >70 :
    print("geçti)







kilo =float(input("Kilo"))
boy =float(input("Boy "))

float endex = kilo /boy*boy *1000
if endex < 18.4 :
    print("zayıf")
elif 18.5<endex<24.9 :
    print("normal")
elif 25<endex<29.9:
    print("fazla kilolu")
else:
    print("obez")








sayilar =[1,2,3,4,5,6,7,8,9,10,11,12,13]
for sayi in sayilar:
    print(sayi)

isimler =["ali","bob","veli"]
for isim in isimler:
    print(isim)

tupe =[(1,2,),(3,4),(5,6),(7,8)]
for i,j in tupe:
    print(i,j)

name= "Ali"
for n in name:
    print(n)

d = {"k1":1, "k2":2, "k3":3}
for key,value in d.items():
    print(key, value)

result =list(range(50))
for i in  result:
    print(result[i])

for i in range(5):
    print(i)
for i in range(10,20,2):
    print(i)
saylar = [1,2,3,4,5,6,7,8,9,10,11]
for  i in saylar:
    if i %3 ==0:
        print(i)


toplam =0
for i in saylar:
    toplam +=i
print(toplam)

sayilar = [1,2,3,4,5,6,7,8,9]
teksayi=[]
for i in teksayi:
    if i%2 ==1:
        teksayi.append(i)

for i in teksayi:
    print(i)
    '''

urunler = [
  {'name':'samsung S6', 'price': '3000' },
  {'name':'samsung S7', 'price': '4000' },
  {'name':'samsung S8', 'price': '5000' },
  {'name':'samsung S9', 'price': '6000' },
  {'name':'samsung S10', 'price':'7000'}
]
toplam = 0
for urun in urunler:
   fiyat = int(urun['price'])
   toplam += fiyat
print('toplma ürün fiyatı:',toplam)


for urun in urunler:
  if (int(urun['price']) <= 5000):
     print(urun['name'])