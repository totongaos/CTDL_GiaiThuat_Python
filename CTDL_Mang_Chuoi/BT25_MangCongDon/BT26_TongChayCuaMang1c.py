# Cho mảng nums chứa các số nguyên,
# bạn hãy tìm một mảng chứa các số nguyên thỏa mãn điều kiện runningSum[i] = sum(nums[0]…nums[i]).
'''Với đầu vào được nhập từ bàn phím: 1 2 3 4
Kết quả đầu ra in ra màn hình là: 1 3 6 10'''

# nums = [1, 6, 3, 2, 7, 2]
nums = [int(x) for x in input().split()]
def prefix_array(nums):
    #1. tạo mảng nums_prefix
    nums_prefix = [nums[0]]
    for index in range(1,len(nums)):
        nums_prefix.append(nums[index]+nums_prefix[-1])
    return nums_prefix

print(*prefix_array(nums))