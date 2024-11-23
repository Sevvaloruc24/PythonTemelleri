# value type => number,string
x=4
y=26
x=y
y=46          # y de yaptığımız bir değişiklik x'i etkilemez.
print(x,y)    # verinin kendisi ile ilgilenilir.


# reference type => list,class
a=['pant','shirt']
b=['pant','shirt']
a=b
b[0]='skirt' # b'deki değişiklik a'yı etkiliyor.
# reference tipinde adres ile ilgileniyoruz.
#atama işleminde tek adreste oldukları için herhangi bir listedeki ddeğişiklik hepsini etkiliyor.
print(a,b)