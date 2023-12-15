# Cho mảng nums chứa n số nguyên, trong đó các số nguyên đã được sắp xếp theo thứ tự không giảm,
# bạn hãy thực hiện bình phương từng số nguyên,
# sau đó đầu ra hiển thị mảng chứa các giá trị bình phương tương ứng trên cũng theo thứ tự không giảm.

# Việc bình phương mỗi phần tử và sắp xếp mảng mới cực kỳ đơn giản,
# tuy nhiên, bạn có cách nào để tìm được một đáp án theo cách khác với độ phức tạp tính toán O(n) hay không?
# Lưu ý: Hãy chú ý trường hợp số âm !!!


#1. input mảng arr_1
# arr = [int(x) for x in input().split()]
# print(arr)
arr = [-8,0,3,6,7,9]

# HÀM SẮP XẾP NổI BỌT
def bubbleSort(arr):
    #1. sắp xếp lại mảng
    for j in range(1, len(arr)):
        swapped = True
        for i in range(1,len(arr)):
            if abs(arr[i]) < abs(arr[i-1]):
                arr[i-1], arr[i] = abs(arr[i]), abs(arr[i - 1])
                swapped = False
        if swapped:
            break
    #2. input lại mảng arr là số bình phương của chính nó
    for i in range(1, len(arr)):
        arr[i] = arr[i]*arr[i]
    return arr
#2. print theo yc đề bài
print(*bubbleSort(arr))

