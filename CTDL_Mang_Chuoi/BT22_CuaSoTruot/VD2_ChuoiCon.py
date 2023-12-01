# Cho một chuỗi nhị phân s. Chỉ có duy nhất một lần chuyển 0 thành 1.
# Sau khi thực hiện việc chuyển, độ dài của chuỗi con dài nhất chỉ chứa 1 là bao nhiêu?
# Ví dụ: cho s = 1101100111, đáp án là 5. Khi ta thực hiện thao tác ở chỉ số 2, chuỗi sẽ trở thành 1111100111.
'''thay vì chuyển 0 thành 1 thì ta sẽ xài 1 biến để đếm số lượng số 0. (count_0)'''

#1. input string s
str_s = '11001'
#2. đổi string -> list
arr = list(str_s)

#HÀM CỬA SỔ TRƯỢT
def slidingWindow(arr):
    #1. khai báo biến left, count_0, len_arr = 0
    left, count_0, len_arr = 0,0,0
    #2. xài vòng lặp for để chạy cửa right
    for right in range(0, len(arr) - 1):
        #2.1 check phần tử nào = 0
        if arr[right] == '0':
            count_0 += 1 #tăng biến count_0 lên 1 đơn vị
        #2.2 xài vòng lặp while check đã gặp số 0 thứ 2 chưa?
        while count_0 > 1:
            #2.2.1 check arr[left] == '0'?
            if arr[left] == '0':
                count_0 -= 1 #nếu = 0 thì giảm biến đếm 0 xuống 1 đơn vị để lúc nào cũng chỉ có 1 số 0
            # 2.2.2 nếu arr[left] != '0' thì di chuyển cửa left qua phải 1 bước đến khi nào gặp số 0 đầu tiên?
            left += 1
        #2.3 tính độ dài của mảng con chưa 1 số 0 và các số 1 liên tiếp
        len_arr = max(len_arr, right - left + 1)
    return len_arr
print(slidingWindow(arr))