website = 'http://www.sadikturan.com'
course = 'Python Kursu: Baştan Sona Python Programlama rehberiniz (40 saat)'

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini siliniz.
message = ' Hello World '
message = message.strip()
print(message)
#message=message.lstrip()    #leftstrip
#message=message.rstript()   #rightstrip

# 2- 'www.sadikturan.com' içindeki sadik turan bilgisi haricindeki her karakteri siliniz.
message='www.sadikturan.com'
message=message.strip('w.moc')
print(message)
# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapınız.
course = 'Python Kursu: Baştan Sona Python Programlama rehberiniz (40 saat)'
course=course.lower()
print(course)

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
website = 'http://www.sadikturan.com'
website=website.count('a')
print(website)

# 5- 'website' www ile başlayıp com ile bitiyor mu ?
website = 'http://www.sadikturan.com'
website=website.endswith('com')
print(website)

website = 'http://www.sadikturan.com'
website=website.startswith('www')
print(website)
# 6- 'website' içinde '.com' ifadesi var mı ?
website = 'http://www.sadikturan.com'
website=website.find('.com')
print(website)

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi ? (isalpha,isdigit)
course = 'Python Kursu: Baştan Sona Python Programlama rehberiniz (40 saat)'
course=course.isalpha()
print(course)

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result='Contents'
result=result.center(50)
print(result)

# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '_' ile değiştiriniz.
course = 'Python Kursu: Baştan Sona Python Programlama rehberiniz (40 saat)'
course=course.split(' ')
print(course)
course=('_').join(course)
print(course)

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştiriniz.
s='Hello World'
s=s.replace('World','There')
print(s)

# 11- 'course' karakter dizisini boşluk karakterlerinden ayırınız.
course = 'Python Kursu: Baştan Sona Python Programlama rehberiniz (40 saat)'
course=course.split()
print(course)
