sayilar=[1,3,5,7,9,12,19,21]

# 1- sayilar listesini while ile ekrana yazdırınız.
i=0
while(i<len(sayilar)):
    print(sayilar[i])
    i+=1

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm sayıları ekrana yazdırın.
bas=int(input('başlangiç değeri gir:'))
bit=int(input('bitiş değeri gir:'))
bas+=1
while(bas<bit):
    print(bas)
    bas+=1

# 3- 1-100 arasındaki tek sayiları azalan şekilde yazdırınız.
bas=1
son=100
while(son>bas):
    if son%2==1:
        print(son)
    son-=1

# 4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırınız.
numbers=[]  # Boş liste açtım.
i=0
while(i<5):
    sayi=int(input('sayi gir:')) # Döngü içerisinde sayilar istendi.
    numbers.append(sayi) # Append merodu ile her sayı sona eklendi.
    i+=1
numbers.sort() # liste sayı büyüklüğüne göre sıralandı.
print(numbers)
    
# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız
#    ** ürün sayısını kullanıcıya sorun.
#    **dictionary listesi yapısı(name,price) şeklinde olsun.
#    **ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyiniz.

urunler=[]                       # Ürün listesi açtık.

urunsayisi=int(input('laç adet ürün gerekli:')) 

i=0
while(i<urunsayisi):
    name=input('ürün ismi:')     # Döngü içerisinde isim ve fiyat istendi.
    price=float(input('ürün fiyati:'))
    urunler.append({             # Liste içerisine ekleme yaptık.
        'name':name,
        'price':price
    })
    i+=1

print(urunler)
    
    

