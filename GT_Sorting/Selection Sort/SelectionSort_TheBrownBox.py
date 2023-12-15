# WAY1:
def selectionSort(arr,n):
    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]: #tim min trong khoang [i+1:n+1]
                min_index = j
        if min_index != i:
            arr[i],arr[min_index] = arr[min_index],arr[i]
        print(f'i-{i} : {arr}')
    return arr

arr = [8,5,1,2,0]
n = len(arr)
print(selectionSort(arr,n))