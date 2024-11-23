maasAli = 5000
maasAhmet = 4000
vergi = 0.27
print(maasAli-(maasAli*vergi))
print(maasAhmet * vergi)
# değişken tanımlama kuralları
# rakam ile başlayamaz
#büyük küçük harf duyarlılığı vardır. Örneğin; küçük != Küçük gibi
# türkçe karakter kullanmayalım
# isim tanımlanırken arada boşluk  olamaz
x= 1                 # int
y = 2.3              # float
name = "Çinar"       # string \ karakter
isStudent = True     # bool
 
 # veri tipi dönüşümleri

#x = input("1. sayi:")
#y = input("2.sayi:")
#toplam = x + y
#print(toplam)   # input u string olarak algılıyor
# print(type(x))
# print(type(y))
# toplam = int(x)+int(y)
# print(toplam)

'''
daire alani:π(r*2)
daire çevresi:2πr
yaricapi verilen bir dairenin alan ve çevresini hedaplyiniz
'''
pi=3.14
r=float(input('yariÇap:'))
alan= pi*(r**2)
çevre=2*pi*r
print('alan:',alan)
print('çevre:',çevre)



