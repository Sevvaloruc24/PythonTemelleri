# 1- Girilen iki sayıdan hangisi büyüktür?
a=int(input('1. sayi giriniz:'))
b=int(input('2. sayi giriniz:'))
result=(a>b)
print(f'a:{a} b:{b} den büyüktür:{result}')

# 2- Kullanıcıdan 2 vize(%60) ve final (%40) notunu alıp ortalama hesaplayınız.Eğer ortalama  50 ve üstündeyse geçti değilse kaldı yazdırınız.

vize1=float(input('1. vize notu:'))
vize2=float(input('2. vize notu:'))
final=float(input('1. final notu:'))

ortalama=((vize1+vize2)*(0.6))+final*0.4
result=bool(ortalama>=50)
print(f'not ortalamaniz:{ortalama} ve dersten geçme durumunuz:{result}')

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırınız.

sayi=int(input('sayi:'))
tekcift=(sayi%2==0)
print(f'girilen sayini çift olma durumu:{tekcift}')

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.

sayi=float(input('sayi giriniz:'))
negpoz=(sayi>0)
print(f'sayinin pozitiflik durumu:{negpoz}')

# 5- Parola ve email bilgisi isteyip doğruluğunu kontrol ediniz.  (email: email@sadikturan.com  parola:abc123)

parola=input('parola giriniz:')
email=input('email giriniz:')
result=(parola=='abc123')
result2=(email=='email@sadik turan.com')

print(f'parola doğruluk değeriniz:{result} ve email doğruluk durumunuz:{result2}')
