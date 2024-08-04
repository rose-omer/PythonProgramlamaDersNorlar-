name = "Ali"
surname = "kara"
age = 36
print(name + surname)
print(age)
greeting  = "Hello My name is  " + name + " " + surname+"\nI m  "+str(age)+"  years old"
print(greeting)
print("My name is {} {}".format(name,surname))
print("My name is {1} {0}".format(name,surname))
print("My name is {n} {n}".format(n=name,s=surname))
print("My name is {} {} and I'm {} years old.".format(name, surname , age))
print("My name is {0} {0} and I'm {0} years old.".format(name))
print(f"My name is {name} {surname} and I'm {age} year sold.")
greeting  = "Hello My name is  " + name + " " + surname+"\nI m  "+str(age)+"  years old"
result1 = greeting[0]
result2 = greeting[12]
print(result1)
print(result2)
result3 = greeting[-1]
print(result3)
result4 = len(greeting)
print(result4)
result5 = greeting[len(greeting)-1]
print(result5)
result6 = greeting[0:20]
print(result6) #Hello My name i
result7 = greeting[:7]
print(result7)
result8 = greeting[3:]
print(result8)
result9 = greeting[0:12:2]
print(greeting)
print(result9)
result10 = greeting[::-1]
print(result10)
website = "http://www.mehmetakif.edu.tr"
course = "Python Dersi: Baştan Sona Python Programlama Dersi(14Hafta)"
x ="corse"
y = "website"
result11 = len(x)
print(result11)
result12 = len(y)
print(result12)
length1 = len(x)
length2 = len(y)
print("course karakter dizisinde {} adet karakter vardır".format(len(x)))
print("website  karakter dizisinde {} adet karakter vardır".format(len(y)))
result13 = website[7:10]
print(result13)
result13=website[26:28]
print(result13)
result14=website[len(website)-2:len(website)]
print(result4)
result15=len(course)
print(result15)
print(course[0:15])
print(course[15:])
print(course[-15:])
print(course[::-1])
name, surname, age ,job ="ayşe ", "yılmaz " , 18 ,"CITIR"
print("Benim adım {} {} ,Yasım {} ve mesleğim {} ".format(name,surname,age,job))
result16= "abc" * 3;
print(result16)
message = 'Hello, There.'
message2 = message.split(',')
message3 =message.upper()
print(message3)
message4 = "merhaba yazılım mühendisliği umamrım hojdur "
print(message4.title())
print(message4.capitalize())
username = "           ömerfaruköse      "
x =username.strip()
print("My username  is {}".format(username))
username1 ="..... ömerfaruk köse!?"
y = username1.strip(".,?,!")
print("My username is {}".format(y))

message4 = "My username is ÖMER "
print(message4)
message4 = message4.replace("ÖMER "," FARUK ")
print(message4)
message5 = "My name is ömer"
message6 = message5.find("name")
print(message6)
website = "http://www.mehmetakif.edu.tr"
course = "Python Dersi: Baştan Sona Python Programlama Dersi(14Hafta)"
a ="  hello world  "
a = a.strip()
print(a)
result = " Hello World ".strip()     # baş ve sondaki boşluk karakterleri silinir.
result = " Hello World ".lstrip()    # baştaki boşluk karakterleri silinir.
result = " Hello World ".rstrip()    # sondaki boşluk karakterleri silinir.
result =   website.lstrip("/:pth")   # baştan itibaren '/:pth' karakterinekadarsilinir.



result01 = "http://www.mehmetakif.edu.tr".strip('/:pthw.edu.tr')
print(result01)
deneme =course.lower()
print(deneme)
deneme =course.upper()
print(deneme)
deneme =course.title()
print(deneme)
ara =website.count("a")
print(ara)


result = website.count('a')         # a karakteri sayılır.
print(result)
result = website.count('www')       # www karakterleri sayılır.
print(result)
result = website.count('www',0,10)  # 0 ile 10. indeks arasında www ifadesi sayılır.
print(result)
course = "Python Dersi: Baştan Sona Python Programlama Dersi (14 Hafta)"
result = course.isalpha()   # tüm karakterler alfabetik mi diye sorar ve False gelir.
print(result)
result = 'Hello'.isalpha()  # tüm karakterler alfabetik olduğundan True geli# r.
print(result)
result = course.isdigit()   # tüm karakterler rakam mı diye sorar ve False gelir.
print(result)
result = '123'.isdigit()    # tüm karakterler rakam mı diye sorar ve True gelir.
print(result)
result = course
course = "Python Dersi: Baştan Sona Python Programlama Dersi (14 Hafta)"
result = course.isalpha()   # tüm karakterler alfabetik mi diye sorar ve False gelir.
print(result)
result = 'Hello'.isalpha()  # tüm karakterler alfabetik olduğundan True gelir.
print(result)
result = course.isdigit()   # tüm karakterler rakam mı diye sorar ve False gelir##
print(result)
result = '123'.isdigit()    # tüm karakterler rakam mı diye sorar ve True gelir.
print(result)
mersaj = "Hello World ".replace("World", "there ")
print(mersaj)
mersaj1= course.split(" ")
print(mersaj1)
def metin_istatistikleri(metin):
    # Metni paragraflara ayır
    paragraflar = metin.split('\n')
    paragraf_sayisi = len(paragraflar)

    # Paragraflar üzerinde döngüye girerek istatistikleri hesapla
    toplam_cumle = 0
    toplam_kelime = 0
    toplam_karakter = 0

    for paragraf in paragraflar:
        # Paragraf içindeki cümleleri say
        cumleler = paragraf.split('.')
        toplam_cumle += len(cumleler)

        # Paragraf içindeki kelime sayısını bul
        kelimeler = paragraf.split()
        toplam_kelime += len(kelimeler)

        # Paragraf içindeki karakter sayısını bul
        toplam_karakter += len(paragraf)

    # Sonuçları yazdır
    print("Toplam Paragraf Sayısı:", paragraf_sayisi)
    print("Toplam Cümle Sayısı:", toplam_cumle)
    print("Toplam Kelime Sayısı:", toplam_kelime)
    print("Toplam Karakter Sayısı:", toplam_karakter)

# Kullanıcıdan metin girişi al
metin = input("Metni girin:\n")

# Metin istatistiklerini hesapla ve yazdır
metin_istatistikleri(metin)
