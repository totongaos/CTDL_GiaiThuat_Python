'''Nhập vào một số nguyên dương n, và n số nguyên lần lượt là các phần tử trong dãy a.
Tiếp theo nhập vào hai số nguyên là k và x (0 ≤ k ≤ n).

Hãy chèn phần tử có giá trị x vào dãy a, ở trước phần tử có chỉ số k và sau phần tử có chỉ số k-1.
In mảng kết quả ra màn hình, mỗi số cách nhau bởi một khoảng trắng.

Giải thích: Với n = 4, a = [1, 2, 3, 4], k = 1, x = 10.
Ta sẽ chèn phần tử 10 vào dãy a ở trước phần tử ở index k =1.
'''
#1. input số phần tử n của mảng arr
n=int(input())
# n=3
#2. input các phần tử của arr
arr = [int(x) for x in input().split()]
arr.append("")#để tý chèn phần tử ko bị lỗi "index out of range"
# print(arr)
#3. input index_k và phần tử x
k, x = [int(y) for y in input().split()]
# print(k,x)

#4. chèn phần tử
for i in reversed(range(k+1,n+1)):
    print(i)
    arr[i] = arr[i-1]
arr[k] = x
#5. print theo yc đề
print(*arr)
# for i in range(n+1):
#     print(arr[i], end=" ")