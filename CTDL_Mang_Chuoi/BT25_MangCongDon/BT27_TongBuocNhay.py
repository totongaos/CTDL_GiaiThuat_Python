# Cho mảng nums có các phần tử là các số nguyên.Tìm 1 số nguyên dương bất kỳ startValue.
# Trong mỗi vòng lặp, lần lượt tính tổng của số nguyên dương đó với các số nguyên trong mảng theo thứ tự từ trái sang phải.
# Kết quả thu được một giá trị là sumArray.
#
# Hãy tìm số nguyên dương startValue nhỏ nhất để sao cho tổng sumArray không nhỏ hơn 1.

# nums = [1, 2, 1, 4, 2]
nums = [int(x) for x in input().split()]
def prefix_array(nums):
    minVal = 1
    sumVal = 0
    count = 0
    for index in range(0,len(nums)):
        sumVal += nums[index]
        minVal = min(minVal,sumVal)
    while minVal <= 1:
        minVal+=1
        count += 1
    return count
    # return -minVal +1

print(prefix_array(nums))