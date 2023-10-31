# Nhập và hai tự nhiên a và b. Hãy tính giá trị của a mũ b = a* chính a với số lần b

# a = int(input())
# b = int(input())
a=2
b=3

def factorials(a,b):
    if b == 0:
        return 1
    else:
        return a*factorials(a,b-1)

print(factorials(a,b))