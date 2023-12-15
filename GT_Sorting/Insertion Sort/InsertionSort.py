# Nhập vào số nguyên dương n, tiếp theo là n số nguyên của dãy số a.
# Hãy sắp xếp dãy số a thành dãy không giảm (số sau không bé hơn số trước) và in dãy đó ra màn hình,
# sau mỗi phần tử có đúng một khoảng trắng.

# n = int(input())
# arr = [int(input()) for i in range(n)]
#
arr = [9, 1, 3, 7, 8, 4, 2, 6, 5]
n=9
def insertionSort(arr):
    # k =0
    # Lặp qua tất cả các phần tử trong mảng
    for i in range(1,len(arr)):
        value = arr[i]
        # Di chuyển tất cả các phần tử của mảng mà lớn hơn key về sau 1 vị trí
        index = i -1
        while index >=0 and value < arr[index]:
            arr[index+1], arr[index]= arr[index], arr[index+1]
            index -= 1
        arr[index + 1] = value
    return arr

print(*insertionSort(arr))