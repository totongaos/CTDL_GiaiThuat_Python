'''Yêu cầu bài toán:
Ở một vương quốc nọ, có một nhà toán học thiên tài tên là Euler đã tìm ra một nguyên lý hết sức đặc biệt,
có thể dẫn đến việc xây dựng được một công cụ toán học cho một trò chơi số học thú vị đó là:
"một số nguyên dương bất kỳ đều có thể phân tích được dưới dạng tích của các thừa số nguyên tố."
Ví dụ: 6=2*3, 100=2*2*5*5.

Nhà vua của vương quốc khá thích thú với điều này và đã tạo ra một trò chơi số học như sau:
Người chơi sẽ chọn một số nguyên dương n. # Sau đó, tại mỗi vòng chơi, sẽ thay thế n bằng tổng các thừa số nguyên tố của nó
(ví dụ 315=3*3*5*7 thì 315 sẽ được thay thế bằng số 3+3+5+7=18).
Cứ như vậy cho đến khi số cuối cùng không thể chuyển đổi thành một số khác được nữa thì trò chơi sẽ dừng lại
và người chơi theo vòng tại lượt chơi đó sẽ chiến thắng. Hãy viết chương trình tìm số cuối cùng thu được theo nguyên tắc trên.
'''

#way 1:
from math import sqrt
#1. tao ham check_Prime(a) : check num có phải số nguyên tố hay không?
def check_Prime(a):
    for i in range(2,int(sqrt(a))+1):
        if a%i == 0 :
            return False
    if a >1: # để chắc rằng số 2&3 ko bị sót
        return True
    else:
        return False

#2. tạo hàm find_FirstNumIsDiv(n) tìm số nguyên tố đầu tiên mà num chia hết
def find_FirstNumIsDiv(n):
    #2.1 xài vòng lặp for chạy từ 1 -> n
    for i in range(n+1):
        if check_Prime(i): #2.1.2 check i có phải số nguyên tố ko
            if n%i==0: #2.1.2 check n%i ko
                return i #nếu có return i
    return n #nếu ko return n


#3. tạo hàm TroChoiSoHoc(n)
def TroChoiSoHoc(n):
    #4 check n có phải số nguyên tố ko với hàm check_Prime(n)
    if check_Prime(n):#4.1 nếu là số nguyên tố return n
        return n
    else: #4.2 nếu ko phải số nguyên tố
        lst = [] #4.2.1 tạo mảng lst để chứa các số nguyên tố mà n chia hết
        m = n #4.2.2 cho m = n
        #4.2.3 xài vòng lặp while với đk m ko phải số nguyên tố.
        while check_Prime(m) == False:
            temp = find_FirstNumIsDiv(m) #tạo biến tạm temp chứa số nguyên tố đầu tiên mà num chia hết qua hàm find_FirstNumIsDiv(m)
            m = m//temp #cho m = m//temp
            lst.append(temp) #append biếntemp vào lst
            #=> chạy vòng lặp đến khi m là số nguyên tố
        lst.append(m) #4.2.4 append m vào lst
        # print(lst)
        return TroChoiSoHoc(sum(lst)) #4.2.5 dequy TroChoiSoHoc(sum(lst)) -> tìm số cuối cùng thu được theo nguyên tắc trên.

n=315
# n=int(input()) #1. input n
# print(find_FirstNumIsDiv(n))
print(TroChoiSoHoc(n)) #2. truyền n vào hàm TroChoiSoHoc(n) & print


#way 2:
from math import sqrt
#Cần tìm tổng của các thừa số nguyên tố tại mỗi bước chơi
def SumPrimeFactors(n):
    Sum = 0 #1. Gán một biến sum có giá trị khởi tạo là 0.

    while n%2==0: #2. Trong khi n chia hết cho 2
        Sum += 2 #2.1. cộng 2 vào tổng sum
        n=n//2   #2.2 chia n cho 2
    #3. Sau bước 2,n phải là số lẻ. Bây giờ bắt đầu một vòng lặp từ i = 3 đến căn bậc hai của n. Trong khi n chia hết cho i,
    # thì ta cộng i vào sum và chia n cho i, tăng i lên 2 và tiếp tục.
    for i in range(3,int(sqrt(n))+1,2):
        while n%i == 0:
            Sum += i
            n = n//i

    #4. Nếu n là số nguyên tố và lớn hơn 2 thì sẽ không thể thực hiện theo hai bước trên.
    # Vì vậy, cộng vào sum nếu nó lớn hơn .
    if n>2:
        Sum += n
    return Sum

#Liên tiếp thực hiện các bước chơi cho đến khi kết quả của tổng bằng chính số cuối cùng sau khi biến đổi.
def TroChoiSoHoc(n):
    while n != SumPrimeFactors(n):
        n = SumPrimeFactors(n)
    return n

n = 315
# n=int(input()) #1. input n
print(TroChoiSoHoc(n))