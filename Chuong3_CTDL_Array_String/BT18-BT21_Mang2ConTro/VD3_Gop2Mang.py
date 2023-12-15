# Cho hai mảng số nguyên đã sắp xếp.

# Trộn hai mảng và trả về mảng mới cũng được sắp xếp.

# arr_1 = [int(x) for x in input().split()]
# arr_2 = [int(x) for x in input().split()]
arr_1 = [2,3,8,11]
arr_2 = [1,5,8,9]


def array_OfTwoPoint(arr_1,arr_2):
    index1 = index2 = 0
    arr_final = []
    while index1 < len(arr_1) and index2 < len(arr_2):
        if arr_1[index1] < arr_2[index2]:
            arr_final.append(arr_1[index1])
            index1 += 1
        elif arr_1[index1] > arr_2[index2]:
            arr_final.append(arr_2[index2])
            index2 += 1
        else:
            arr_final.append(arr_1[index1])
            arr_final.append(arr_2[index2])
            index1 += 1
            index2 += 1

    #make sure both iterables are exhausted
    while index1 < len(arr_1):
        arr_final.append(arr_1[index1])
        index1 += 1

    while index2 < len(arr_2):
        arr_final.append(arr_2[index2])
        index2 += 1
    return arr_final

print(array_OfTwoPoint(arr_1,arr_2))