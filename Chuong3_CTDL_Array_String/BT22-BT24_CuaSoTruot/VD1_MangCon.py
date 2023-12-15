# Cho một mảng số nguyên dương nums và một số nguyên k.
# Tìm độ dài của mảng con dài nhất có tổng nhỏ hơn hoặc bằng k.

arr = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8

def slidingWindow(arr,k):
    left, sum_k, len_arr = 0,0,0
    for right in range(0, len(arr) - 1):
        sum_k += arr[right]
        while sum_k > k :
            sum_k -= arr[left]
            left += 1
        len_arr = max(len_arr, right - left + 1)
    return len_arr
print(slidingWindow(arr,k))