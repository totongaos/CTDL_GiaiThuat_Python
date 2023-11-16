def square(x):
  if (x == 0):
    return x
  else:
    # square(x - 1)
    # print((2*x)-1)
    return square(x-1) + (2*x) - 1
'''
x=1 +2*1-1 =1
x=2 +2*2-1 =3
x=3 +2*3-1 =3
'''
x=3
print(square(x))
