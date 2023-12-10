def merge(arr1,arr2):
    n = len(arr1) + len(arr2)
    res = [0] * n
    i, i1, i2 = 0, 0, 0
    while i<n:
        if i1<len(arr1) and i2<len(arr2): # arr1 & arr2 != Empty
            if arr1[i1] <= arr2[i2]:
                res[i] = arr1[i1]
                i+=1
                i1+=1
            else:
                res[i] = arr2[i2]
                i+=1
                i2+=1
        else: # arr1 or arr2 == Empty
            if i1 < len(arr1): #arr1 != Empty
                res[i] = arr1[i1]
                i+=1
                i1+=1
            else: #arr2 != Empty
                res[i] = arr2[i2]
                i += 1
                i2 += 1
    return res


def mergeSort(arr , L , R):
    # Case dac biet DK dung
    if L>R: return [0]
    if L==R:
        single_element = [arr[L]]
        return single_element

    # Case tong quat

    # Chia ra
    print("Chia: " , L , '-' , R)
    k = (L+R)//2
    arr1 = mergeSort(arr,L,k)
    arr2 = mergeSort(arr,k+1,R)

    # Tron Vao
    res = merge(arr1,arr2)
    print('kqua merge: ', res)
    return res


if __name__ == '__main__':
    arr = [1, 5, 3, 2, 8, 7, 6, 4]
    print(mergeSort(arr,0,len(arr)-1))

    # a = [1,5,7]
    # b = [3,4,9]
    # print(merge(a,b))