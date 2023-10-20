# Cho số nguyên dương n, tiếp theo là n số nguyên cũng một dãy a, cuối cùng là một số x, biết dãy là dãy không giảm.
# Hãy đưa ra chỉ số của phần tử đầu tiên có giá trị bằng x, nếu không tồn tại giá trị đó đưa ra -1.



# n = int(input())
# a = [int(input()) for i in range(n)]
# x = int(input())
a = [1,1,2,2,3,3,4,4,5]
x = 7
for i in range(0,len(a)):
    if a[i] == x: print(i);break
print(-1)