liste = ["apple", "banana", "cherry"]
liste.append("orange")   #append ekleme komutu
print(liste)

liste.insert(3, "karpuz")   # insert ara index ekleme
print(liste)

liste.remove("karpuz")      # remove eleman silmeye yarıyor
print(liste)

liste.pop()          # sondakini silmne
print(liste)

del  liste[2]           # del index ile siler index vermexsen komple siler
print(liste)

liste.clear()           # clear komle siler
print(liste)


a = ["apple", "banana"]
b = ["orange", "cherry"]
a=b
b[0]="Update"
print(a,b)

a = ["apple", "banana"]
b = ["orange", "cherry"]
a=b.copy()
b[0]="Update"
print(a,b)


a = ["apple", "banana"]
b = ["orange", "cherry"]
a=list(b)
b[0]="Update"
print(a,b)

letters =["a " ,"g" , "h"]
number =[1,2,5,4,6]
number.sort()
print(number)
number.reverse()
print(number)

print(max(number))
print(min(number))
print(max(letters))
print(min(letters))


number=[1,2,3,4,5,6,7,8,9]
letters=["a","b","c","d","g","j"]
number.count(10)
letters.count("a")
names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000,1998,1987]

names.append("Cenk")
print(names)
names.insert(0,"İrem")
print(names)
names.insert(-1 , "Mehmet")
print(names)
names.insert(len(names), "Ömer")
print(names)
names.remove("Deniz")
names.pop()
names.pop(3)
print(names)
names = ['Ali','Yağmur','Hakan','Deniz']

resault = "Ali" in names
print(resault)
names.reverse()
print(names)
names.sort()
print(names)
names.sort(reverse=True)
print(names)
years.sort()
print(years)
str ="Audi,Bmw,Fiat"
print(str.split(","))
print(max(years))
print(min(years))
resault2 = years.count(1998)
print(resault2)
years.clear()
del years
print("3 marka  gir ")
a =input()
b =input()
c =input()
marka =[]
marka.append(a)
marka.append(b)
marka.append(c)
print(marka)
print("3 sayı gir ")
sayi1 = input()
sayi2 = input()
sayi3 = input()

sayilar =[]
sayilar.append(sayi1)
sayilar.append(sayi2)
sayilar.append(sayi3)
print(max(sayilar))
print(min(sayilar))



print(" iki sayı gir")
a =input()
b =input()

if a<b:
    print("b a'dan büyüktür ")
elif a==b:
    print("a b birbirine eşittir ")
elif a>b :
    print("a b den büyüktür")


num = int(input('sayı: '))

if num > 0:
    print('sayı pozitif')
elif num < 0:
    print('sayı negatif')
else:
    print('sayı sıfır')

usurname =input("kullanacı adı gir")
password = input("pasaport gir ")
if (usurname== "ömer"):
    if (password == "ömer123"):
        print("Hoş geldiniz ")
    else:
        print("parola yanlış")
else:
    print("kullanıcı adı yanlış")


if(usurname == "ömer " and password == "ömer123"):
    print("hoşgeldin knk ")
else:
    print("kullanıcı adı veua şifre yanlış ")
