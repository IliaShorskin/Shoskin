pamyat = 1.44
a = pamyat*1024*1024		
simbols = 25*50*100*4
b = round(a / simbols, 0)
c = int(b)

print("Количество книг, помещающихся на дискету:", c)