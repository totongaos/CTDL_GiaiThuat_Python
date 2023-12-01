# Cho mảng số nguyên nums
# Có bao nhiêu cách chia mảng thành 2 phần
# sao cho tổng của phần bên trái >= bên phải và phần bên phải có ít nhất 1 phần tử.

#way 1: sử dụng mảng cộng dồn và biến left_arr, right_arr
# nums = [7, 5, 2, -4]
# def prefix_array(nums):
#     #1. tạo mảng nums_prefix
#     nums_prefix = [nums[0]]
#     for index in range(1,len(nums)):
#         nums_prefix.append(nums[index]+nums_prefix[-1])
#     print(nums_prefix)
#     #2. tạo biến đếm count
#     count = 0
#     #3. xài vòng lặp for để tách mảng trái & phải
#     for i in range(0, len(nums)-1):
#         left_arr = nums_prefix[i]
#         right_arr =  nums_prefix[-1] - nums_prefix[i]
#         if left_arr >= right_arr:
#             count+=1
#     return count
#
# print(prefix_array(nums))

# --------------------------------------------------
# # way 2:sử dụng mảng cộng dồn
# nums = [7, 5, 2, -4]
# def prefix_array(nums):
#     #1. tạo mảng nums_prefix
#     nums_prefix = [nums[0]]
#     for index in range(1,len(nums)):
#         nums_prefix.append(nums[index]+nums_prefix[-1])
#     print(nums_prefix)
#     #2. tạo biến đếm count
#     count = 0
#     #3. xài vòng lặp for để tách mảng trái & phải
#     for i in range(0, len(nums)-1):
#         if nums_prefix[i] >= nums_prefix[len(nums)-1] - nums_prefix[i]:
#             count+=1
#     return count
#
# print(prefix_array(nums))


# --------------------------------------------------
# way 3:không sử dụng mảng cộng dồn
nums = [7, 5, 2, -4]
def prefix_array(nums):
    #1. tính tổng mảng nums
    sum_nums = sum(nums)
    #2. tạo biến đếm count
    count = left_arr =  0
    #3. xài vòng lặp for để tách mảng trái & phải
    for i in range(0, len(nums)-1):
        left_arr += nums[i]
        right_arr = sum_nums - left_arr
        if left_arr >= right_arr:
            count+=1
    return count

print(prefix_array(nums))