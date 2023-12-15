'''
Ex: input: nums = [3, 2, 2, 3] val=3
    output: 5, nums= [2, 2]

Explanation: Your function should return len = 2, with the first two element of nums being 2
For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accept
'''

def remove_element(nums, val):
    n = len(nums)
    i = 0
    while i < n:
        if nums[i]==val:
            for j in range(i,n-1):
                nums[j] = nums[j+1]
            n-=1
        else:
            i+=1

    return f'n: {n} | {nums}'

if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    print(remove_element(nums,2))