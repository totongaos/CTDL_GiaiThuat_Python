# Hải có một dãy số gồm n số nguyên, Hải muốn sắp xếp các phần tử của dãy đó với các yêu cầu sau:
#
# Từ trái qua phải:
# Các số nguyên dương xuất hiện theo giá trị tăng dần.
# Các số nguyên âm xuất hiện theo giá trị giảm dần.
# Không thay đổi vị trí của phần tử mang giá trị 0.
# Không thay đổi tính chất ở mỗi vị trí
# -> (Nghĩa là nếu trước khi sắp xếp vị trí i có giá trị nguyên âm thì sau khi sắp xếp vị trị i cũng phải mang giá trị âm,
# nếu ví trị i mang giá trị dương cũng tương tự).
# Cho trước dãy a. Hãy sắp xếp theo cách của Hải. In kết quả ra màn hình, sau mỗi phần tử có đúng một khoảng trắng.
# Với a = [3, -1, 2, 0, -4, 6] thì kết quả mong muốn là "2 -1 3 0 -4 6 ".
# Giải thích:
# Các số nguyên dương xuất hiện theo thứ tự tăng dần 2, 3, 6.
# Các số nguyên dương xuất hiện theo thứ tự giảm dần -1, -4.

def quickSort(arr_last,L,R):
    i,j = L,R
    pivot = arr_last[(L+R)//2]

    while i<j:
        while arr_last[i]<pivot:
            i+=1
        while pivot<arr_last[j]:
            j-=1
        if i<=j:
            arr_last[i],arr_last[j] = arr_last[j],arr_last[i]
            i+=1
            j-=1

    if i < R:
        quickSort(arr_last,i,R)
    if L<j:
        quickSort(arr_last,L,j)
    return arr_last

# n = int(input())
# arr = [int(input()) for i in range(n)]
n= 6
arr = [9,1,-7,0,-3,0]
arr_last = []

for i in range(0,len(arr)):
    if arr[i]!= 0:
        arr_last.append(arr[i])
# print(arr,arr_last)

R = len(arr_last)-1
quickSort(arr_last,0,R)

# print(arr,arr_last)
k=0
for e in range(1,len(arr)+1):
    if arr[len(arr)-e]<0:
        arr[len(arr)-e] = arr_last[k]
        k+=1
for d in range(0,len(arr)):
    if arr[d]>0:
        arr[d] = arr_last[k]
        k+=1
print(*arr)




#way 1: ko xai giai thuat
# n = int(input())
# arr = [int(input()) for i in range(n)]
# arr_last = []
#
# for i in range(0,len(arr)):
#     if arr[i]!= 0:
#         arr_last.append(arr[i])
#
# arr_last.sort()
#
# k=0
# for e in range(1,len(arr)+1):
#     if arr[len(arr)-e]<0:
#         arr[len(arr)-e] = arr_last[k]
#         k+=1
# for d in range(0,len(arr)):
#     if arr[d]>0:
#         arr[d] = arr_last[k]
#         k+=1
# print(*arr)
