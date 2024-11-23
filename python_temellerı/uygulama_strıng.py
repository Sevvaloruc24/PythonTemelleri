website = 'http://www.sadikturan.com'
course = 'Python Kursu: Baştan Sona Python Programlama Rehberinix (40 saat)'

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
print(len(course)) #len dizi uzunluğunu verir.

# 2- 'website' içinden www karakterlerini alın.
print(website[7:10]) #soldan indeks 0'dan başlar

# 3- 'website' içinden com karakterlerini alın.
print(website[22:25])

# 4- 'course' içinden ilk 15 ve son 15 karakterleri alın.
print(course[0:15])
print(course[-15:])

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
print(course[::-1])

name,surnema,age,job='Bora', 'Yilmaz',32, 'mühendis'

# 6- Yukarıda verilen değişkenler ile ekrana aşağidaki ifadeyi yazdırın.
# 'Benim adim Bora Yılmaz, Taşim 32 ve mesleğim mühendis.'
print(f'Benim adim {name} {surnema} , Taşim {age} ve mesleğim {job}')

# 7- 'Hello World' ifadesindeki w harfini 'W' ile değiştirin.
s='Hello world'
s= s[0:6] +'W'+ s[-4:]
print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdirin.
a='abc'*3
print(a)



