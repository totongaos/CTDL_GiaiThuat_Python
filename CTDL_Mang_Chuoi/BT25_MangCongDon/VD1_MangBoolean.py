# Cho một mảng số nguyên nums, một mảng queries trong đó queries[i] = [x, y] và một số nguyên limit.
# Hãy tạo mảng boolean trả về kết quả của từng truy vấn.
# Một truy vấn là true nếu tổng của mảng con từ x đến y nhỏ hơn limit, ngược lại là false.

nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13

def prefix_array(nums, queries, limit):
    #1. tạo mảng nums_prefix
    nums_prefix = [nums[0]]
    for index in range(1,len(nums)):
        nums_prefix.append(nums[index]+nums_prefix[-1])

    #2. tạo mảng boolean_arr
    boolean_arr = []
    #3. taọ biến sum_queries chứa sum của index trong queries
    sum_queries = 0

    #4. xài vòng lặp for để lấy index trong mảng queries
    for x, y in queries:
        #4.1 tính sum_queries theo các index trong mảng queries
        sum_queries = nums_prefix[y] - nums_prefix[x] + nums[x]
        #4.2 append kqua 'true' or 'false' vào mảng boolean_arr
        boolean_arr.append(sum_queries < limit)
    return boolean_arr

print(prefix_array(nums, queries, limit))
