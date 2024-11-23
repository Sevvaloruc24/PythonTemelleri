# 1- 'BMW, Mercedez, Opel, Mazda' elemanlarına sahip bir liste oluşturunuz.
my_list=['BMW','Mercedez','Opel','Mazda']

# 2- Liste kaç elemanlıdır?
print(len(my_list))

# 3- Listenin ilk ve son elemanı nedir?
print(my_list[0])
print(my_list[-1])       
print(my_list)

# 5- Mercedes listenin bir elemanı mıdır? 
result=my_list
result= 'Mercedez' in my_list                # in operatörü kullanılır.
print(result)

# 6- Listenin -2 indeksindeki değeri nedir?
print(my_list[-2])

# 7- Listenin ilk üç elemanını alın.
my_list=my_list[0:3]
print(my_list)

# 8- Listenin son 2 elemanı yerine 'Toyota' ve 'Renault' değerlerini ekleyin.
my_list=['BMW','Mercedez','Opel','Mazda'] 
my_list[2:]=['Toyota','Renault']
#my_list[-1]='Renault'                       # stringdeki gibi replace kullanmaya gerek yoktur.
#my_list[-2]='Toyota'                        # stringdeki gibi replace kullanmaya gerek yoktur.
print(my_list)

# 9- Listenin üzerine 'Audi' ve 'Nissan' değerlerini ekleyin.
a=['Audi','Nissan']
my_list=my_list + a
print(my_list)

# 10- Listenin son elemanını silin.
my_list=['BMW','Mercedez','Opel','Mazda']
del my_list[-1]                              # del operatörü silme işleminde kullanılır.
print(my_list)

# 11- Liste elemanlarını tersten yazdırın.
my_list=['BMW','Mercedez','Opel','Mazda']
print(my_list[::-1]) # baştan sona -1 geri adım ile yazdırılır.


# 12- Aşağıdaki verileri bir liste içinde saklayınız.

    #studentA: Yiğit Bilgi 2010, (70,60,70) 
studentA=['Yiğit','Bilgi',2010,[70,60,70]]
    #studentB: Sena Turan 1999, (80,80,70)
studentB=['Sena','Turan',1999,[80,80,70]]
    #studenC: Ahmet Turan 1998, (80,70,90)
studentC=['Ahmet','Turan',1998,[80,70,90]]
list=studentA+studentB+studentC

# 13- Liste elemanlarını ekrana yazdırınız.
print(studentA[0])
print(studentA[1])
print(studentA[2])
print(studentA[3][0])
print(studentA[3][1])
print(studentA[3][2]) # studentB ve studentC için de aynısı yapılır.