# Nhập vào số nguyên dương n, tiếp theo là n số nguyên của dãy số a.
# Hãy sắp xếp dãy số a thành dãy không giảm (số sau không bé hơn số trước) và in dãy đó ra màn hình,
# sau mỗi phần tử có đúng một khoảng trắng.

# n = int(input())
# arr = [int(input()) for i in range(n)]
#
arr = [4,3,1,5]
n =4
def insertionSort(arr):
    # Lặp qua tất cả các phần tử trong mảng
    for i in range(1,len(arr)):
        value = arr[i]
        # Di chuyển tất cả các phần tử của mảng lớn hơn key về sau 1 vị trí
        index = i -1
        while index >=0 and value < arr[index]:
            arr[index+1]= arr[index]
            index -= 1
        arr[index + 1] = value
    return arr

print(*insertionSort(arr))