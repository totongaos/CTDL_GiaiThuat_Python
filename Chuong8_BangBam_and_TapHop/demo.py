

key = 'sua'
#Su dung vong lap
cuahang = ['banhmi', 'sua', 'keo']
found = False
for i,k in enumerate(cuahang):
    if key == k:
        cuahang[i] = key
        print(key,k)
        found = True