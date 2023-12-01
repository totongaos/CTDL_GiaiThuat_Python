# Cho một mảng số nguyên dương nums và một số nguyên k.

# Hãy trả về số lượng mảng con chứa các phần tử được xếp đúng theo thứ tự của mảng gốc,
# trong đó tích của tất cả các phần tử trong mảng con nhỏ hơn k.

arr = [10, 5, 2, 6]
k = 100
class Solution():
    def slidingWindow(self,arr,k):
        if k <= 1:
            return 0
        left, sum_k, len_arr = 0, 1, 0
        for right in range(0, len(arr)):
            sum_k *= arr[right]
            while sum_k >= k :
                sum_k //= arr[left]
                left += 1
            len_arr += right - left + 1
        return len_arr
print(Solution.slidingWindow('',arr,k))