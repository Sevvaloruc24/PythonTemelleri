fruits={'orange', 'apple', 'banana'}      # set tanımlaması süslü parantez ile

#print(fruits[3]) indekslenemez bir liste

for x in fruits:
    print(x) # basit bir döngü içerisinde elemanları yazar.
# elemanlar sıralanamıyor.
fruits.add('cherry')
fruits.update(['mango','grape']) # update metodu ile liste içerisine yeni bir liste gönderebiliriz.
# olan bir eleman varsa yazmaz elemanı tekrarlamaz, her elemandan bir tane bulunur.
fruits.remove('mango') # silinir.
fruits.discard('apple')  # silinir.
fruits.pop() # liste sıralı olmadığından son elemanın silineceği garantilenmez.
fruits.clear() # set teki bütün elemanlar silinir.


print(fruits)






#myList=[1,2,5,4,4,2,1]
#print(set(myList)) # set e çevirdik tekrarlayan eleman tek yazıldı.









