# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerinş isteyip ehliyet alabilme durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 yaş ve eğitim durumu lise ya da 
# üniversite olmalıdır.

name=input('name:')
age=int(input('age:'))
edu=input('edu:')
if age>=18:
    if edu=='lise' or edu=='üniversite':
        print(f'{name} ehliyet alabilir')
else:
    print(f'{name} ehliyet alamaz')
 
# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
# 0-24   => 0
# 25-44  => 1
# 45-54  => 2
# 55-69  => 3
# 70-84  => 4
# 85-100 => 5

yazili1=float(input('not gir:'))
yazili2=float(input('not gir:'))
sözlü=float(input('not gir:'))
ortalama=(yazili1+yazili2)*0.4+sözlü*0.6

if 0<=ortalama<=24 :
    print('notunuz 0')
elif  25<=ortalama<=44:
    print('notunuz 1')
elif  45<=ortalama<=54:
    print('notunuz 2')
elif  55<=ortalama<=69:
    print('notunuz 3')
elif  70<=ortalama<=84:
    print('notunuz 4')
else:
    print('notunuz 5')


# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
# 1. Bakım => 1. yıl
# 2. Bakım => 2. yıl
# 3. Bakım => 3. yıl
# ** Süre hesabını alınan gün , ay , yıl bilgisine göre gün bazlı hesaplayınız.
# *** datetime modülünü kullanmanız gerekiyor.
# (simdi) - (2018/8/1) => gün


