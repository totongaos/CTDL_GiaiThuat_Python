# Nhập vào số nguyên dương n, tiếp theo là n số nguyên của dãy số a.
# Hãy sắp xếp dãy số a thành dãy không giảm (số sau không bé hơn số trước) và in dãy đó ra màn hình,
# sau mỗi phần tử có đúng một khoảng trắng.


# n = int(input())
# arr = [int(input()) for i in range(n)]
#
arr = [3,2,1,3,4,5]

#WAY 2:
def selectionSort(arr):
		# tạo vòng lặp chạy từ đầu đến cuối mảng a
    for j in range(0, len(arr)):
				# hãy coi biến đầu tiên là biến nhỏ nhất trong dãy
        min = j
				# tạo vòng lặp từ biến tiếp theo đến hết dãy
        for i in range(0+j,len(arr)):
            if arr[min] > arr[i]:
                min = i
				# đổi chỗ vị trí của số thấp nhất với biến đầu tiên của mảng
        if arr[min]!=arr[j]:
            arr[j],arr[min]=arr[min],arr[j]
    return arr

print(*selectionSort(arr))



#WAY 1:
#


