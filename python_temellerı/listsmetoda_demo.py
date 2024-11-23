names=['Ali','Yağmur','Hakan','Deniz']
years=[1998 ,2000, 1998, 1987]

# 1- 'Cenk' ismini listenin sonuna ekleyiniz.
names=names+['Cenk']
print(names)

# 2- 'Sena' ismini listenin başına ekleyiniz.
names.insert(0,'Sena')
print(names)

# 3- 'Deniz' ismini listeden siliniz.
#names.pop(4)
print(names)

# 4- 'Deniz' isminin indeksi nedir?
print(names.index('Deniz')) # index operatörü ile yerini belirliyoruz.

# 5- 'Ali' listenin bir elemanı mıdır?
result= 'Ali' in names
print(result)

# 6- Liste elemanlarını ters çeviriniz.
names.reverse()
print(names)
print(years.reverse())

# 7- Liste elemanlarını alfabetik olaraka sıralayınız.
names.sort()
print(names)

# 8- years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)

# 9- str='Chevrolet,Dacia'  karakter dizisini listeye çeviriniz.
str='Chevrolet,Dacia' 
print(str.split(',')) # split metodu ile listeye çevirebiliyoruz.

# 10- year dizisinin en büyük ve en küçük elemanı nedir?
print(min(years))
print(max(years))

# 11- years dizisinde kaç tane 1998 değeri vardır?
print(years.count(1998))

# 12- years dizisinin tüm elemanlarını siliniz.
print(years.clear())

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar=[]  # öncelikle boş bir liste ayarlanır.
marka=input('marka:') # input ile yazılacak marka istenir.
markalar.append(marka) # append metodu ile listeye ekleriz.
print(markalar) # ve yazdığımız marka listeye yazılır.

