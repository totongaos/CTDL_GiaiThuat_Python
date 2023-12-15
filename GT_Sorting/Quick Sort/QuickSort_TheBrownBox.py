# Return pivot value
def partition(arr,L,R,key):
    iL = L
    iR = R
    while iL <= iR:
        #voi iL -> find p.tu >= key
        while arr[iL] < key: iL+=1

        #voi iR -> find p.tu <= key
        while arr[iR] > key: iR-=1

        #doi vtri 2 p.tu dang dung k dung vtri
        if iL <= iR:
            arr[iL], arr[iR] = arr[iR], arr[iL]
            iL += 1
            iR -= 1

    return iL

def quickSort(arr, L, R):
    #DK Dung:
    if L>=R: return

    #b1. chon key
    key = arr[(L+R)//2]

    #b2. phan bo lai mang theo key
    k = partition(arr,L,R,key)

    #b3. chia doi mang => lap lai
    quickSort(arr, L, k-1)
    quickSort(arr, k, R)
    return arr

if __name__ == '__main__':
    arr = [6,7,8,5,4,1,2,3]
    print(quickSort(arr,0,len(arr)-1))
    print('DONE')