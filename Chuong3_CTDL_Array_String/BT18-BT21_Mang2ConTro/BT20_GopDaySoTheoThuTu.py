# Cho hai dãy số nguyên đã được sắp xếp theo thứ tự không giảm a và b với số phần tử lần lượt là m và n.
# Hãy viết chương trình gộp hai dãy số nguyên a và b thành một dãy số nguyên c, sao cho dãy c cũng là dãy không giảm.
# Sau đó, hãy in dãy c ra màn hình, sao cho sau mỗi phần tử in ra của dãy có đúng một dấy cách.

#1. input m
# m = int(input())
m = 4
#2. input mảng a
arr_1 = [int(x) for x in input().split()]
print(arr_1)
# arr_1 = [2,3,8,11]
#3. input n
# n = int(input())
n = 4
#4. input mảng b
# arr_2 = [int(x) for x in input().split()]
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

print(*array_OfTwoPoint(arr_1,arr_2))