# defining recursive functions
def func1(n):
  if (n <= 5) :
    print(n, end=' ') #prints n
    n+=1         #increments n by 1
    func2(n)      #calls func2()
  else:
    return

def func2(n):
  if (n <= 5) :
    print(n, end=' ')  # prints n
    n+=1            # increments n by 1
    func1(n)       # calls func1()
  else:
    return

n=0
func1(n)
