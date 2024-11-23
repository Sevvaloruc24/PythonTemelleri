x=5
hak=5
devam='e'
result=5<x<10

# and , bir adet false false yapar
result= x>5 and x<10 
result=(hak>0) and (devam=='e')

# or  , bir adet true true yapar
result=(x>0) or (x&2==0)

# not , tam tersi değer

result=not(x>0)

print(result)
