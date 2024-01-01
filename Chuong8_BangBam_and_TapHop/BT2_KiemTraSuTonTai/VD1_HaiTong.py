'''
Cho một mảng số nguyên nums và số nguyên target.
Trả về chỉ số của 2 số có tổng bằng target (2 chỉ số khác nhau).
'''

class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            #lay tung p.tu trong nums để tìm tong = target
            num = nums[i]
            complement = target - num
            # print(num , complement)
            if complement in dict:
                return [i,dict[complement]]
            dict[num] = i

        return "Sorry I couldn't find it !!!"

if __name__ == '__main__':
    nums = [12, -4, 4, 5, 7, 8, 0, -3]
    target = 10
    vd1 = Solution()
    print(vd1.twoSum(nums,target))

