# Nhập vào một số nguyên dương n, tiếp theo nhập n số nguyên lần lượt là các phần tử của dãy a.
# Hãy in ra những phần tử lẻ ở chỉ số chẵn, sau mỗi phần tử có đúng một dấu cách, nếu không có phần tử nào thõa mãn thì in ra "NULL".

n = 9
a = [1,1,2,2,3,3,4,4,5]

# n = int(input())
# a = [int(input()) for i in range(n)]

result = True
for i in range(0, n):
    if i % 2 == 0:
        if a[i] % 2 != 0:
            print(a[i], end=" ")
            result = False
if result:
    print("NULL")