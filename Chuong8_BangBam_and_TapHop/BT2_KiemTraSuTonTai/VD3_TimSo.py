'''
Cho mảng số nguyên nums, tìm tất cả các số x thỏa mãn điều kiện sau: x + 1 và x - 1 đều không thuộc nums.
'''

class Solution:
    def findNumber(self, nums):
        res = []
        # chuyển đổi nums thành tập hợp
        seen = set(nums)
        for x in nums:
            if (x+1 not in seen) and (x-1 not in seen) :
                res.append(x)

        return res

if __name__ == '__main__':
    nums = [1,2,9,4,50,6]
    vd3 = Solution()
    print(vd3.findNumber(nums))

