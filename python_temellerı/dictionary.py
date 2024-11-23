# key - value

# 41 => kocaeli , 34 => istanbul temsil edilecek şekilde yapmak istiyoruz.

#sehirler=['kocaeli','istanbul']
#plakalar=['41','34']
#print(plakalar[sehirler.index('kocaeli')])         # 41 değerini veriyoruz.

# print(plakalar['kocaeli']) => 41
# print(plakalar['istanbul']) => 34

#plakalar={'kocaeli':41,'istanbul':34}              # key:value , süslü parantez kullanılır.
#print(plakalar['kocaeli'])
#print(plakalar['istanbul'])

#plakalar['ankara']=6                               # yeni eleman alınır.
#print(plakalar) 
#plakalar['kocaeli']='new value'                    # key e yeni bir value ataması yapılır.
#print(plakalar) 

user={
    'sadikturan':{
        'age':36,
        'roles':['user'],
        'email':'sadikturan@gmail.com',
        'address':'kocaeli',
        'phone':'13234234'
    },
    'cinarturan':{
         'age':2,
         'roles':['admin','user'],
        'email':'cinar@gmail.com',
        'address':'kocaeli',
        'phone':'13234234',
    },
}

print(user['cinarturan']['roles'][1])
