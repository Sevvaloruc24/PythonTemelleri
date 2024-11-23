x,y,z=5,10,20 # atama bu şekilde daha kolay yapılabilir.Ayrı ayrı yazılması gerekmez.
#x,y=y,xvvv # içerikler değişir.

# x+=4
# x*=5
# x/=5
# x%=5
# y=y**5

# print(x,y,z)


values=1,2,3
print(values)
print(type(values))  # tuple liste
x,y,z=values         # her liste değerini sırası ile değişkene atıyor.
values=1,2,3,4,5
x,y,*z=values # x ve y'ye ilk iki değer atanır.Ancak geriye kalanlar z'ye liste şeklinde atanır.


print(x,y,z)
print(x,y,z[1])
print(x)
print("sevval")
