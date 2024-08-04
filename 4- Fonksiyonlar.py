def hello():
    print("Hello")

hello()


def isim(name):
    print("Hello " + name)

isim("Ömer")


def isim2(name):
    return "Hello " + name

print(isim2("Sami"))


def toplama(a,b):
    return a+b
sonuc = toplama(5,8)

print(sonuc)


def carpma(a,b):
    return a*b

sonuc = carpma(5,8)
print(sonuc)

def modalma(a,b):
    return a%b

sonuc = modalma(12,3)
print(sonuc)

def yashesapla(dogumYili):
    return 2024- dogumYili

ageÖmer = yashesapla(2002)
ageSami = yashesapla(2004)
ageİsmail = yashesapla(2003)

print(ageSami, ageÖmer , ageİsmail)

'''
def emeklilikNe(dogumYili , isim ):
    yas =yashesapla(dogumYili)
    emeklilik= 65- yas
    if emeklilik > 0 :
        print("emekliliğinize"+emeklilik+"yıl kaldı")
    else:
        print("Zaten emeklisin")

print(emeklilikNe(1983 , "Ali"))
print(emeklilikNe(1950 , "Ayşe"))
print(emeklilikNe(1974 ,"Ömer"))
'''


'''
def yazdır(kelime , kaçkere):
    for i in range(kaçkere):
        print(kelime)

yazdır("ömer" ,5)
# 2-	Gönderilen 2 sayı arasındaki tüm asal sayıları bulan python fonksiyon uygulamasını yapınız.
def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
             else:
                 print(sayi)

sayi1 = int(input("sayı 1:"))
sayi2 = int(input("sayı 2:"))

asalSayilariBul(sayi1,sayi2)

def tamBÖlenleri(sayi1):
    sayilar =[] 
    for i in range(sayi1):
         if sayi1 % i == 0:
             sayilar.append(i)
tamBÖlenleri(20)
'''

square = lambda num :num**2
print(square(5))

a = lambda a,b, c  : a+b+c
print(a(1, 2, 3))

numbers = [1,2,3,4,5,6,7,8,9,10]
def square(num):
    return num**2

result = list(map(square, numbers))
print(result)


numbers = [1,2,3,4,5,6,7,8,9,10]
check_even = lambda num : num % 2 == 0
print(check_even(numbers[2]))


x ="gLOBAL X"
def function():
    x ="local x"
    print(x)

function()
print(x)

""" ----------------------------------------------"""
""" ----------------------------------------------"""
""" ----------------------------------------------"""

''' Kapsama alanlarından bi soru gelir '''

""" ----------------------------------------------"""
""" ----------------------------------------------"""
""" ----------------------------------------------"""


def ctoF(derece):
    fahrenayt =derece*9/5+32
    print(fahrenayt)

ctoF(123)
celcius = input(print("DERECE GİR"))

def ctoF2(derece):
    fahrenayt =derece*9/5+32
    return int(fahrenayt)
ctoF2(celcius)

ömerhesap ={
    "ad" : "ömer köse"

}