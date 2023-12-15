# WAY1:
def insertionSort(arr,n):
    for i in range(1,n):
        arr_i = arr[i]
        j = i-1
        while j>=0 and arr_i<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = arr_i
        print(f'i-{i} : {arr}')
    return arr

arr = [1,5,1,2,9]
n = len(arr)
print(insertionSort(arr,n))