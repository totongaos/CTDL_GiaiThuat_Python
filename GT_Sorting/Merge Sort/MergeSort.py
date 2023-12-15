# n = int(input())
# a = [int(input()) for i in range(n)]

n = 5
arr = [2,6,7,0]
def mergeSort(arr):
    #check len(arr) có lơn hơn 1 ko? ban đầu len arr > 1
    if len(arr)>1:
        #tính index mid của mảng
        mid_idx = len(arr) // 2

        #cho L_half là nửa đầu của mảng
        L_half = arr[:mid_idx]
        # print(len(L_half))
        # cho R_half là nửa đầu của mảng
        R_half = arr[mid_idx:]
        # print(len(R_half))

        #xài đệ quy để tách các phần tử trong mảng còn 1 phần tử
        mergeSort(L_half)
        #xài đệ quy để tách các phần tử trong mảng còn 1 phần tử
        mergeSort(R_half)
        print(len(R_half), len(L_half))
        index_L,index_R,index_arr=0,0,0 #tạo các bien index cho mảng L, R, arr

        #chạy vong lap while với dk len của mảng trái, phải > index. bđ index = 0
        while index_L<len(L_half) and index_R<len(R_half):
            #so sánh để sắp xếp vào mảng mới
            if L_half[index_L] < R_half[index_R]:
                arr[index_arr] = L_half[index_L]
                index_L+=1
            else:#so sánh để sắp xếp vào mảng mới
                arr[index_arr] = R_half[index_R]
                index_R += 1
            index_arr += 1
        # chạy vong lap while với dk len của mảng trái > index.
        while index_L<len(L_half):
            arr[index_arr] = L_half[index_L]
            index_L+=1
            index_arr+=1
        # chạy vong lap while với dk len của mảng phải > index.
        while index_R<len(R_half):
            arr[index_arr] = R_half[index_R]
            index_R+=1
            index_arr+=1

    return arr


print(mergeSort(arr))