'''
Give two sorted integer arrays nums1 & nums2, merge nums2 into nums1 as one sorted array
The number of elements initialized in nums1 & nums2 are m & n respectively.
You may assume that num1 has a size equal to m+n such that it has enough space to hold additional elements from nums2
Ex1: input: nums1 = [1,2,3,0,0,0], m=3, nums2 = [2,5,6], n=3
     output: [1]
'''

def insertArray(nums1,m,nums2,n):
    isFind_k = False
    i = m-1
    j = n -1
    k = (m+n)-1
    while k >= 0:
        if j<0:
            nums1[k] = nums1[i]
            i-=1
        elif i<0:
            nums1[k] = nums1[j]
            j -= 1
        elif nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1

if __name__ == '__main__':
    nums1 = [1,2,3,3,0,0,0]
    nums2 = [2,7,8]

    print(insertArray(nums1,4,nums2,3))
    print('DONE')
