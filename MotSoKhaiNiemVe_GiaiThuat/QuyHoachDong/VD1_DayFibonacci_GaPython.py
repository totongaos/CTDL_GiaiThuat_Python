'''
Thuật toán Quy Hoạch Động
'''

#way 2: lưu trực tiếp vào mảng
def fibonacci(n):
    f = [0,1,1]
    if n == 1 or n == 2:
        result = f[1]
    else:
        for i in range(2,n+1):
            f.append(f[i-1] + f[i])
    return f[n], f
n=int(input())
print(fibonacci(n))