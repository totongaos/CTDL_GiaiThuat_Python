# Cho một mảng đã sắp xếp gồm các số nguyên phân biệt và số nguyên target.

# Trả về true nếu tồn tại một cặp số có tổng bằng target, ngược lại trả về false.


# arr = [1, 2, 4]
arr = [int(x) for x in input().split()]
target = 22
print(arr)
def array_OfTwoPoint(arr,target):
    left = 0
    right = len(arr) - 1
    while left < right:
        sum_num = arr[left] + arr[right]
        if sum_num == target:
            return True
        elif sum_num > target:
            right -= 1
        else:
            left += 1
    return False
print(array_OfTwoPoint(arr,target))