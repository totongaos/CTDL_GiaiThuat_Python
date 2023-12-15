# Trong diễn biến dịch Covid-19 đang diễn ra khá phức tạp, việc tuyền truyền cách phòng tránh dịch là rất quan trong,
# gọi a[i] là tọa độ của người thứ i,
# khoảng cách giữa hai người i và j là |a[i]-a[j]|.
# Một người có thể truyền được thông tin đến người khác nếu khoảng cách giữa họ không vượt quá k.
#
# Để tuyền truyền thông tin nhanh chóng thì người ta sẽ chỉ truyền thông tin cho 1 số người ban đầu,
# sau đó họ sẽ truyền thông tin cho người khác, Hãy đưa ra số lượng ít nhất là số người ban đầu cần truyền thông tin,
# để sao cho tất cả mọi người đều tiếp cận được thông tin.

# n = int(input())
# arr = [int(input()) for i in range(n)]
# k = int(input())

n= 100
arr = [20139,23343,28524,20939,10264,23776,18348,6986,5664,28547,17623,8913,10161,21146,9074,417,25757,13314,18935,
       29724,2123,20437,31016,6350,21677,18318,22178,8363,4465,29806,1461,21655,2940,14623,17011,5164,10388,5784,13063,
       12727,25436,2112,25417,20355,17286,27478,7823,8795,9796,30096,7109,15690,27391,32514,12224,19109,22604,9026,31183,
       22091,19740,32202,16019,3372,4658,1437,25873,5640,24539,19502,18950,26489,27609,9085,23930,16180,5024,28547,16024,
       7820,30405,9936,18877,28728,5555,18035,19663,15189,18592,15642,21968,1967,8895,4474,20403,22332,5559,18417,24942,22761]
k=1
L = 0
R = len(arr) - 1

def quickSort(arr, L, R):
    i,j = L,R
    pivot = arr[(L+R) // 2]
    while i < j:
        while arr[i]<pivot:
            i += 1
        while pivot < arr[j]:
            j -= 1

        if i <= j:
            arr[i],arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    if i < R:
        quickSort(arr,i,R)
    if L < j:
        quickSort(arr,L,j)
    return arr

# quickSort(arr, L, R)
count = 0
for i in range(1,n):
    # print((arr[i] - arr[i - 1]))
    if (arr[i] - arr[i - 1]) > k:
        print((arr[i] - arr[i - 1]))
        count += 1
if count == 0:
    print(1)
else:
    print(count)