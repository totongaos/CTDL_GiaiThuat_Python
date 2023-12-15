# Nhập vào một số nguyên dương n.
# Hãy in ra tất cả chuỗi nhị phân có độ dài n, các chuỗi sắp xếp tăng dần theo thứ tự từ điển, sau mỗi chuỗi có đúng một dấu cách.

# n = int(input())
n=2

def binary(n, s):
    if n == 0:
        print(s,end=" ")
    else:
        for i in range(0,2):
            binary(n-1,s+ str(i))

binary(n,"")
