'''satır=int(input("Lütfen satır sayısı giriniz "))
yıldız=1
bosluk=satır-1

for i in range(satır):
    for i in range(bosluk):
        print(" ",end="")
    for j in range(yıldız):
        print("*",end="")
    yıldız=(satır*2)-1
    bosluk=bosluk-1
    print()
    '''
'''while True:
    sayı = int(input("Lütfen 0 ve 20 arasında bir sayı giriniz"))
    
   
    if((sayı<=20) and (sayı>=0)):
       
        if sayı%2==1:
          toplam=1     
          for j in range(1,sayı+1):
             toplam=toplam*j
              
        elif sayı%2==0:
            toplam=0
            for a in range(0,sayı+1,1):
              if a%2==0:
                 toplamc=toplamc+a
     print(toplam)            
       else:
       print("tekrar değer giriniz")
    
    '''
'''
import random


karsilama = int(input("Tahmin oyununa hoş geldiniz oynamak istiyorsanız 1 istemiyorsanız 2 girişini yapınız "))

if(karsilama==1):
    sayı = random.randint(1, 100)
    sayac = 0
    while True:
        tahmin = int(input("Lütfen 1-100 arasında bir  tahmin giriniz"))
        if (tahmin>sayı):
            print("Tahmininiz sayıdan büyüktür")
            sayac=sayac+1
        elif(tahmin<sayı):
            print("Tahmininiz sayıdan küçüktür")
            sayac=sayac+1
        if(tahmin==sayı):
             print(f"{sayac} denemenizde buldunuz tebrikler")
             break



elif(karsilama!=1):
    print("Oyuna katılmadınız iyi günler")
'''
'''
import random


karsilama = int(input("Tahmin oyununa hoş geldiniz oynamak istiyorsanız 1 istemiyorsanız 2 girişini yapınız "))

if(karsilama==1):
  zorluk = int(input("Kolay mod için 1 zor mod için 2 girişini yapınız "))
 if(zorluk==1):
          hak=10
 elif(zorluk==2):
          hak=5
 sayı = random.randint(1, 100)
  while True:
   tahmin = int(input("Lütfen 1-100 arasında bir  tahmin giriniz"))
         if(hak==0):
            print("Hakkınız kalmadı oyunu kaybettiniz")
            break
        if (tahmin>sayı):
            print(f"Tahmininiz sayıdan büyüktür ve kalan hak sayınız {hak}")
            hak=hak-1
        elif(tahmin<sayı):
            print(f"Tahmininiz sayıdan küçüktür ve kalan hak sayınız {hak}")
            hak=hak-1
        elif(tahmin==sayı):
             print("Oyunu kazandınız tebrikler")
             break



elif(karsilama!=1):
    print("Oyuna katılmadınız iyi günler")
    '''

'''
for i in range(100):
    if i%3==0 and i%5==0:
        print(i,end=" ")
          '''
'''
metin=input("metin giriniz: ")
for i in range(len(metin)):
 print(metin[i])
'''
'''
secim=int(input("sinema veya tiyatro seçiminizi  sinema için 1 tiyatro için 2 giriniz "))
ogrenci=int(input("ogrenci iseniz 1 ogrenci degilseniz 2 giriniz "))
if(secim==1):
    if(ogrenci==1):
        print("Ücret 7.5 TL ")
    elif (ogrenci == 2):
        print("Ücret 15 TL ")
if (secim == 2):
        if (ogrenci == 1):
         print("Ücret 10 TL ")
        elif (ogrenci == 2):
            print("Ücret 5 TL ")
'''
'''
secim=int(input("Asallığını kontrol etmek istediğiniz sayıyı giriniz "))
sayac=0
for i in range(1,secim):
    if secim%i==0:
        sayac=sayac+1

if (sayac==1):
    print("Girilen sayı asaldır")
if (sayac >1):
    print("Girilen sayı asal değildir")
'''
'''
def alanbul(kenar1,kenar2):
    print(kenar1*kenar2)

kenar1=int(input("Alanını bulmak istediğiniz dikdörtgenin genişliğini giriniz "))
kenar2=int(input("Alanını bulmak istediğiniz dikdörtgenin yüksekliğini giriniz "))
alanbul(kenar1,kenar2)
'''
'''
liste = [3,15,24,12,25,62,10,9,2]
for i in range(0,len(liste)):
    if liste[i]%5==0:
        print(liste[i],end= " ")
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
sayı=int(input("basamak  kontrol etmek istediğiniz sayıyı giriniz "))
kelime=str(sayı)
print(len(kelime))
'''
saat=int(input("Otoparkta geçirdiğiniz süreyi giriniz "))
if (saat<1):
    print("Ücretiniz 10 TL")
if (saat>=1 and saat <5):
    ucret=saat*8
    print("Ücretiniz "+str(ucret)+" TL")
if (saat >=5):
        ucret = saat * 8
        print("Ücretiniz " + str(ucret)+" TL")