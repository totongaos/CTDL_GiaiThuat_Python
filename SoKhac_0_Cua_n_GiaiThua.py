

#way2:
def lastNonZeroDigitFactorial(n, result, sumOf5):
    num = n #1. tạo biến num gán = n

    if num == 1: #2. nếu num = 1 thì trả về 1
        return # base case
    while num%5 == 0: #3. xài vòng lặp while với đk num chia hết cho 5
        num = int(num/5) #3.1 num chia cho 5 đến khi ko chia hết cho 5 nữa
        sumOf5 += 1 #3.2 tăng sumOf5 lên 1 đơn vị cho 1 lần lặp

    while sumOf5 != 0 and (num & 1) == 0: #4. xài vòng lặp while với đk sumOf5!=0 and (num & 1) = 0 =>num phải là số chẵn
        num >>= 1 #4.1 chia num cho 2
        sumOf5 -= 1 #4.2 giảm sumOf5 đi 1 đơn vị

    #5. trả về chữ số cuối khác 0 của giai thừa
    result[0] = (result[0]*(num%10))%10
    lastNonZeroDigitFactorial(n-1,result,sumOf5)

def print_lastNon0Digit(n):
    result = [1]
    lastNonZeroDigitFactorial(n,result, 0)
    return result[0]

# n = int(input())
print(print_lastNon0Digit(7500))