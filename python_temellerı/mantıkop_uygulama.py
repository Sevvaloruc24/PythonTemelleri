# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

a=float(input('sayi giriniz:'))
result=a>0 and a<100
print(f'sayi 0 ve 100 arasında mi:{result}')

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

b=int(input('sayi giriniz:'))
result=b>0 and b%2==0
print(f'sayi pozitif çift sayi mi: {result}')

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.

email=input('email giriniz:')
parola=input('parola giriniz:')
result= (email=='sevoruc@gmail.com') and (parola=='12345')
print(f'giriş yapilabilir mi:{result}')

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

a=int(input('a giriniz:'))
b=int(input('b giriniz:'))
c=int(input('c giriniz:'))

result=a>b and a>c
print(f'a en büyük sayidir:{result}')
result=b>a and b>c
print(f'b en büyük sayidir:{result}')
result=c>a and c>b
print(f'c en büyük sayidir:{result}')

# 5- Kullanıcıdan 2 vize(%60) ve final(%40) notunu alıp ortalama hesaplayınız.Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırınız.

vize1=float(input('vize 1 giriniz:'))
vize2=float(input('vize 2 giriniz:'))
final=float(input('final giriniz:'))
ortalama=float((vize1+vize2)*0.4+(final)*0.6)

#     a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#     b-) Finalde 70 alındığında ortalamanın önemi olmasın.

result=(ortalama>=50 and final>=50) or (final>=70)
print(f'öğrencinin ortalamasi:{ortalama} ve geçme durumu:{result}')

# 6- Kişinin ad , kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#     Formül:(Kilo / boy uzunluğunun karesi)
#     Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#     0-18.4      => Zayıf
#     18.5-24.9   => Normal
#     25.0-29.9   => Fazla kilolu (kilocok)
#     30.0-34.9   => Şişma (obez)

name=(input('isim giriniz:'))
kg=float(input('kilo giriniz'))
hg=float(input('boy giriniz:'))
indeks=float(kg/(hg**2))
zayif=(indeks>=0)and(indeks<=18.4)
normal=(indeks>=18.5)and(indeks<=24.9)
kilocok=(indeks>=25.0)and(indeks<=29.9)
şişman=(indeks>=30.0)and(indeks<=34.9)

print(f'{name} kilo endeksin :{indeks} ve kilo değerlendirmen zayif: {zayif}')
print(f'{name} kilo endeksin :{indeks} ve kilo değerlendirmen normal: {normal}')
print(f'{name} kilo endeksin :{indeks} ve kilo değerlendirmen kilocok: {kilocok}')
print(f'{name} kilo endeksin :{indeks} ve kilo değerlendirmen şişman: {şişman}')
