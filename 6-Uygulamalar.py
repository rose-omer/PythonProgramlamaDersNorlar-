n = int(input("Kaç satırlık piramit çizmek istiyorsunuz? "))
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()



faktoriel =1;
toplam =0;

while True:
    sayi = int(input("0 la 20 arasında gir "))
    if sayi >= 0 and sayi <= 20:
        if sayi%2!=0:
            for i in range(1, sayi+1):
                faktoriel    = faktoriel*i
            print("Girdiğiniz değerin faktöriyeli: ", faktoriel)
        else:
            for j in range(0, sayi+1,2):
                toplam = toplam+j
            print("Girdiğiniz değere kadar olan çift sayı toplamı: ", toplam)
        break
    else:
        print("Belirtilen aralıkta bir değer giriniz!")




import random
cevap =input("oYNAmak istiyormusun ?")
randomSayi= random.randint(0,100)
hak = 1
while cevap ==("EVET"):
    tahmin = int(input("1 ile 100 arasındaki sayıyı tahmin et!"))
    if tahmin == randomSayi:
        print("tahminin doğru tebrik ederim ",hak,"denemede buldun")
        break
    elif tahmin > randomSayi:
        hak+=1
        print("Yanlış, bir dahakine daha küçük bir sayı tahmin et!")
    else:
        hak+=1
        print("Yanlış, bir dahakine daha büyük bir sayı tahmin et!")
        
'''

'''
import random
cevap =input("oYNAmak istiyormusun ?")
seviye =input("zor mu kolay mı ")

randomSayi= random.randint(0,100)
zor = 5
kolay =10
while cevap ==("EVET"):
    if seviye == zor:
        hak =5
        tahmin = int(input("1 ile 100 arasındaki sayıyı tahmin et!"))
        if tahmin == randomSayi:
            print("tahminin doğru tebrik ederim ", hak, "denemede buldun")
            break
        elif tahmin > randomSayi:
            hak -= 1
            print("Yanlış, bir dahakine daha küçük bir sayı tahmin et!")
        else:
            hak -= 1
            print("Yanlış, bir dahakine daha büyük bir sayı tahmin et!")
    elif  hak ==0:
        break


'''


'''
for i in range(0,100):
    if i%3 == 0 and i%5 == 0:
        print(i)
'''
'''
metin = input("metin gir")
for i in metin:
    print(i)


sinemafiyat=15
tiyatoFiyat =20
izle =input("sinema mı tiyatro mu ")
ögrenciMi =input("ögrenci misin")
if "sinema" ==izle:
    if ögrenciMi =="EVET":
        print(sinemafiyat/2 ,"ücret")
    else:
        print(sinemafiyat ,"ücret")
else:
    if ögrenciMi =="EVET":
        print(tiyatoFiyat/2 ,"ücret")
    else:
        print(tiyatoFiyat ,"ücret ")

aslMı =int(input("sayi"))
variable =0
for i in range(2,aslMı):
    if aslMı %i ==0:
        variable=1
if variable==1:
    print("asal değl ")
else:
    print("asal  ")

'''

'''
genişlik =int(input("genislik"))
uzunluk =int(input("uzunluk"))

def alan (genişlik,uzunluk):
    alan=genişlik*uzunluk
    print(alan)
    return alan

alan(genişlik,uzunluk)
def yilin_kacinci_gunu(tarih):
    gun, ay, yil = map(int, tarih.split('-'))
    ay_gun_sayilari = [31, 28 if yil % 4 != 0 or (yil % 100 == 0 and yil % 400 != 0) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    toplam_gun = gun
    for i in range(ay - 1):
        toplam_gun += ay_gun_sayilari[i]
    return toplam_gun

# Örnek kullanım
verilen_tarih = '17-04-2024'
print(f"{verilen_tarih} tarihi {yilin_kacinci_gunu(verilen_tarih)}. gün")
'''
'''

liste = [15, 7, 20, 30, 45, 11, 25]

for i in liste:
    if i %5==0:
        print(i)
'''

'''

ucret=0
boyut=int(input("Pizza boyutunu seçiniz küçük için 1 orta için 2 büyük için 3 "))
if(boyut==1):
    ucret=ucret+25
if (boyut == 2):
        ucret = ucret + 30

if(boyut==3):
    ucret=ucret+35

peynir=int(input("Ekstra peynir ister misiniz 1 evet 2 hayır "))
if(peynir==1):
    if (boyut == 1):
        ucret = ucret + 2
    if (boyut == 2):
        ucret = ucret + 3

    if (boyut == 3):
        ucret = ucret + 3

icecek=int(input("İçecek ister misiniz 1 evet 2 hayır "))
if(icecek==1):
    ucret=ucret+2

print("Toplam ödemeniz gereken ücret "+str(ucret))
'''
'''

sayi =input("sayi gir ")
print(len(sayi))
saat = int(input("saat "))
if saat <1:
    print("ücret 10" )
elif saat>1 and saat<5:
    print("ücret " ,saat*8)
else :
    print("ucret",saat*6)
