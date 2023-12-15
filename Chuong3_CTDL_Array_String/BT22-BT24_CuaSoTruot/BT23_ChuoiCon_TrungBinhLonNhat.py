# Cho mảng nums chứa n số nguyên và cho một số nguyên k.
# Bạn hãy tìm mảng con chứa k số nguyên liên tiếp nhau và có giá trị trung bình của các phần tử là lớn nhất.
# Đầu ra hiển thị giá trị trung bình đó với độ chính xác 5 chữ số sau dấu thập phân.
'''kích thước cố định ko cần đến ký thuật 2 con trỏ'''
arr = [1]
# arr = [int(x) for x in input().split()]
k = 1
class Solution():
    def slidingWindow(self,arr,k):
        if k <= 1:
            return f'{arr[0]:0.5f}'
        sum_k = 0
        for i in range(0,k):
            sum_k += arr[i]
        sum_avg_k = sum_k/(k)
        for right in range(k, len(arr)):
            sum_k += arr[right] - arr[right-k]
            sum_avg_k = max(sum_avg_k, sum_k/(k))
        return f'{sum_avg_k:0.5f}' #return theo yc đề bài
print(Solution.slidingWindow('',arr,k))