# Cho mảng số nguyên nums và số nguyên k.
# Tìm tổng của mảng con có tổng lớn nhất có độ dài là k.
'''kích thước cố định ko cần đến ký thuật 2 con trỏ'''
arr = [3, 6, 4, -5, 9, -1, 2]
k = 4
class Solution():
    def slidingWindow(self,arr,k):
        if k <= 1:
            return 0
        sum_k = 0
        for i in range(0,k):
            sum_k += arr[i]
        sum_final = sum_k
        for right in range(k, len(arr)):
            sum_k += arr[right] - arr[right-k]
            sum_final = (max(sum_final, sum_k))
        return sum_final
print(Solution.slidingWindow('',arr,k))