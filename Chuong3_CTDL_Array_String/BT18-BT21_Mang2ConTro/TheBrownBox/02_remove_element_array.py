'''
Ex: input: nums = [3, 2, 2, 3] val=3
    output: 5, nums= [2, 2]

Explanation: Your function should return len = 2, with the first two element of nums being 2
For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accept
'''

def remove_element(nums, val):
    n = len(nums)
    k = 0
    for i in range(0,n):
        if nums[i]!=val:
            nums[k] = nums[i]
            k+=1
    return f'n: {k} | {nums}'

if __name__ == '__main__':
    arr = [0,1,2,2,3,0,4,2]
    print(remove_element(arr,2))
    print('DONE')