# Nhập vào hai số nguyên a và b. Hãy tìm ước chung lớn nhất của chúng.
#
# (Ước chung lớn nhất của hai số nguyên là một số lớn nhất mà cả hai số đó đều chia hết).


def greatestCommonDivisor(a,b):
    if b==0: return a
    if a%b==0: return b
    return greatestCommonDivisor(b,a%b)


# a = int(input())
# b = int(input())
a = 30
b = 40

print(greatestCommonDivisor(a,b))