'''
Tìm Dãy con tăng dài nhất (Dãy đơn điệu tăng), **dãy con ko liên tiếp + truy vết (ko áp dụng với số 0)**
vd: [1,4,3,5,2] => dãy con là [1,3,5] -> len = 3
'''

#---------------------------------------------
#way 1:
#HAM dynamic_programming
def dynamic_programming(arr,n):
    # 0. Cài thông báo lỗi
    if n == 0:
        return "Mảng rỗng nên ko có dãy con!!!"
    # 0. Fix bug khi mảng chỉ có 1 phần tử
    elif n == 1:
        print(arr[1], end=" ")
        return

    #1. tạo mảng lst luu tru cac do dai cua day con
    lst = [0]*(n+1)
    lst[0] = 1
    lst_trace = [0]*(n+1) #mang truy vet

    #2. xài 2 vòng lặp for lấy index < n && index < i
    for i in range(1,n+1):
        max_len = 0 #reset lại value max_len
        for j in range(0,i):
            if arr[j]<arr[i] and lst[j]>max_len: #so sánh để tìm ra value max_len mới
                # print('arr[j]<arr[i]',arr[j],arr[i], '\tlst[j] > max_len', lst[j], max_len)
                max_len=lst[j]
                lst_trace[i] = j #luu value moc noi tại lst_trace
            lst[i] = max_len + 1 #lưu value max_len+1 tại index i vào mảng lst

    print(f'arr: {arr}\nlst: {lst}\nlst_trace: {lst_trace}')
    print(f'max_len:{max(lst)}')

    #3. TRUY VET
    result = []
    index_Max = lst.index(max(lst))
    while lst_trace[index_Max]:
        # print(lst_trace[index_Max])
        result.append(arr[index_Max])
        index_Max = lst_trace[index_Max] #đang truy vết ngc lại
    result.append(arr[index_Max]) #appned pẩn tử cuối vào mảng
    result = sorted(result)

    return result


#1. input n & mang arr
# n = int(input())
# arr = [int(input()) for i in range(n)]
n = 3
arr = [1,0,3]
arr[:0]=[0] #add 0 vào index-0

#2. chay ham dynamic_programming
print(dynamic_programming(arr,n))
