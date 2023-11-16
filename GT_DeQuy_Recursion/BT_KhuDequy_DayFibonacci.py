#way 1:
def fibonacci(n):
    f = [0,1,1]
    result = 0
    if n == 1 or n == 2:
        result = f[1]
    else:
        for i in range(2,n+1):
            result = f[i-1] + f[i]
            f.append(result)
    return f[n]
n=int(input())
print(fibonacci(n))


#way 2:
def fibonacci(n):
    f = [0,1,1]
    if n == 1 or n == 2:
        result = f[1]
    else:
        for i in range(2,n+1):
            f.append(f[i-1] + f[i])
    return f[n]
n=int(input())
print(fibonacci(n))