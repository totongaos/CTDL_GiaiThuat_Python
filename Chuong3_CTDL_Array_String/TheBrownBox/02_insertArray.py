'''
Give two sorted integer arrays nums1 & nums2, merge nums2 into nums1 as one sorted array
The number of elements initialized in nums1 & nums2 are m & n respectively.
You may assume that num1 has a size equal to m+n such that it has enough space to hold additional elements from nums2
Ex1: input: nums1 = [1,2,3,0,0,0], m=3, nums2 = [2,5,6], n=3
     output: [1]
'''

def insertArray(x,a,m):
    isFind_k = False
    for k in range(0,m):

        if a[k] > x:
            isFind_k = True
            for i in reversed(range(k,m)):
                a[i+1] = a[i]
            a[k] = x
            break
    print(a,m)
    if isFind_k == False:
        a[m]=x
    return a

def merge(n1, m, n2, n):
    for ai in n2:
        insertArray(ai,n1,m)
        m+=1
    return n1
if __name__ == '__main__':
    nums1 = [1,2,3,5,0,0,0]
    nums2 = [6,7,7]

    print(merge(nums1,4,nums2,3))
    print('DONE')
