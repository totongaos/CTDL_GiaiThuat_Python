# WAY1:
def bubbleSort(arr,n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j] , arr[j + 1] = arr[j + 1] ,arr[j]
        print(f'i-{i} : {arr}')
    return arr

arr = [1,5,1,2,9]
n = len(arr)
print(bubbleSort(arr,n))


# -------------------------------
# WAY2: Dừng lại khi dãy đã được sắp xếp xong
def bubbleSort(arr,n):
    for i in range(0, n):
        swapped = True
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                swapped = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f'i-{i} : {arr}')
        if swapped:
            break

    return arr
arr = [3,2,1,7,6]
n = len(arr)
print(*bubbleSort(arr,n))