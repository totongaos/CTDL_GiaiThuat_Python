'''Nhập vào một số nguyên dương n, và n số nguyên lần lượt là các phần tử trong dãy a.
Tiếp theo nhập vào số nguyên là k (0 ≤ k < n).

Hãy xóa phần tử có chỉ số k ở trong dãy đó. In mảng kết quả ra màn hình, sau mỗi phần tử có đúng một khoảng trắng.'''

# n=int(input())
n=3
arr = [int(x) for x in input().split()]
print(arr)
index_k = int(input())

for i in range(0,n):
    if i == index_k:
        arr[i]=arr[i+1]

print(arr)