numbers=[1,10,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']

val=min(numbers)   # min sayı
val=max(numbers)   # max sayı
val=min(letters)   # min harf
val=max(letters)   # max harf

val=numbers[3:6]
val=numbers[:3]
val=numbers[4:]
print(val)


numbers[4]=40

numbers.append(49)             # en sona ekler
numbers.insert(3,78)           # kendinden bir öncekinin yerini alıyor indeks değerine ekliyor.
numbers.insert(-1,52)          
numbers.pop()                  # en sondaki elemanı siliyor.
numbers.pop(0)                 # yazılan indeksteki elemanı siler.
numbers.pop(-1)
numbers.remove(9)              # yazılan karakteri siler.
numbers.sort()                 # sayısal büyüklük olarak liste sıralanır.
letters.sort()                 # alfabetik olarak sıralanır.
numbers.reverse()              # sıralananı tam tersine çevirdi.Tam tersine dizer.
letters.reverse()              # tam tersine çevirir.
print(len(numbers))
print(len(letters))
print(numbers.count(10))       # yazılan sayıdan kaç tane var gösterir.
print(letters.count('a'))      # yazılan karakterden kaç tane var gösterir.
numbers.clear()                # bütün diziyi siler
letters.clear()
numbers.claer()

print(letters)
print(numbers)