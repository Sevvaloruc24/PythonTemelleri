# 3 öğrenci için ekramdan bilgi alındı. Sonrasında numarası yazılan öğreni ile ilgili bilgiler verildi.

ogrenciler={}

number=input('ogrenci no:')
name=input('ogrenci name:')
surname=input('ogrenci surname:')
phone=input('ogrenci phone:')

ogrenciler.update({
    number:{
        'ad': name,
        'soyad':surname,
        'telefon':phone,
    }
})
number=input('ogrenci no:')
name=input('ogrenci name:')
surname=input('ogrenci surname:')
phone=input('ogrenci phone:')

ogrenciler.update({
    number:{
        'ad': name,
        'soyad':surname,
        'telefon':phone,
    }
})
number=input('ogrenci no:')
name=input('ogrenci name:')
surname=input('ogrenci surname:')
phone=input('ogrenci phone:')

ogrenciler.update({
    number:{
        'ad': name,
        'soyad':surname,
        'telefon':phone,
    }
})

print(ogrenciler)

ogrno=input('ogrenci no:')
ogrenci=ogrenciler[number]
print(ogrenci)






