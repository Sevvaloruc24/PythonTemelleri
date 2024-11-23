message='Hello There. My name is Sadik Turan'

#message=message.upper()                       # tum karakterler büyük harfle yazılır.

#message=message.lower()                       # tum karakterler küçük harfle yazılır.
     
#message=message.title()                       # her kelimenin baş harfi büyük harfe çevrilir.

#message=message.capitalize()                  # ilk kelimenin başharfi büyük diğer harfeler küçük.

#message=message.strip()                       # baştaki boşluk karakterini yok eder.

#message=message.split()                       # boşluk karakterlerinden ayrılıp ayrı diziler haline getirir.

#message=message.split('.')                    # noktalardan itibaren ayırır.

#message= '*'.join(message)                    # birleştirirken araya * ekleyecek.

#message=message.find('Sadik')                 # aranılan kelimenin hemen başlamasının önündeki yer.

#message=message.find('Sadikkk')               # olmadiği için -1 cevabini verecek

#message=message.startswith('H')               # verilen ile başlıyor. boşluk dahi başta olsa false verecektir.

#message=message.endswith('H')                 # verilen ile bitiyor.

#message=message.replace('Sadik','Çinar')      # ilkinin yerine ikinciyi yerlesştirir.

#message=message.center(100)                   # 100 karakterlik alan oluşturup ortalanır.

#message=message.center(100,'!')               # sağ ve sola verilen karakteri dahil eder

print(message)