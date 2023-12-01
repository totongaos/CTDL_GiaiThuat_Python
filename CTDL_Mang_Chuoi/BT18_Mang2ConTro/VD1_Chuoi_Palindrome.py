# Viết hàm trả về true nếu chuỗi là palindrome, nếu không trả về false.
# palindrome nếu đọc xuôi và ngược giống nhau.
# Điều đó có nghĩa là sau khi đảo ngược chuỗi thì nó vẫn là chuỗi ban đầu. Ví dụ: abcdcba hoặc tek4ket.

string_a = str(input())
print(string_a)
def array_OfTwoPoint(string_a):
    left = 0
    right = len(string_a) - 1
    while left < right:
        if string_a[left] != string_a[right]:
            return False
        left += 1
        right -= 1
    return True
print(array_OfTwoPoint(string_a))