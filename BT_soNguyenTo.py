'''Cách 1

Ý tưởng để giải quyết vấn đề này là lặp qua tất cả các số bắt đầu từ 2 đến N/2 bằng cách sử dụng vòng lặp `for`
Với mỗi số, hãy kiểm tra xem nó có chia hết cho N không.
- Nếu chúng ta tìm thấy bất kỳ số nào chia hết, chúng ta sẽ trả về `false`.
- Nếu chúng tôi không tìm thấy bất kỳ số nào từ 2 đến N/2 chia hết cho N thì điều đó có nghĩa là N là số nguyên tố và chúng tôi sẽ trả về `True`.

Tuy nhiên, **độ phức tạp tính toán của cách này khá lớn** và có thể không vượt qua được một số giới hạn thời gian của các mẫu thử'''

def check_Prime(a):
    for i in range(2,(a//2)+1):
        if a%i == 0 :
            return False
    if a >1: # để chắc rằng số 2&3 ko bị sót
        return True
    else:
        return False

check_Prime(2)

'''Cách 2

Thuật toán tìm số nguyên tố nhanh nhất. 
Thay vì kiểm tra đến N, chúng ta có thể kiểm tra đến √N vì **thừa số lớn hơn của N phải là bội số của thừa số nhỏ hơn đã được kiểm tra.**
Do đó, thay vì xét đến N/2, chúng ta chỉ cần 1 vòng lặp đến √N. Điều này tiết kiệm hơn nhiều!!!!'''

from math import sqrt
def check_Prime(a):
    for i in range(2,int(sqrt(a))+1): #phải thêm int vô vì căn xong là float
        if a%i == 0 :
            return False
    if a >1: # để chắc rằng số 2&3 ko bị sót
        return True
    else:
        return False
n=int(input())
print(check_Prime(n))