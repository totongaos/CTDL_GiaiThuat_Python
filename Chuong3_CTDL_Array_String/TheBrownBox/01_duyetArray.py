'''
Tìm các số có chữ số chẵn
Find numbers with even numbers of digits
'''
#WAY 1: xai len()
if __name__ == '__main__':
    a = [120, 345, 20, 6, 78962]
    count = 0
    for i in a:
        if len(str(i))%2 == 0:
            count += 1
    print(count)

# #WAY 2: dung ham dem so chu so
# def find_numbers_num(n):
#     count = 0
#     res = n
#     while res != 0:
#         res = n//10
#         n = res
#         count += 1
#     return count
# def find_num(a):
#     count = 0
#     for i in a:
#         num = find_numbers_num(i)
#         if num%2==0:
#             count += 1
#     return count
# if __name__ == '__main__':
#     arr = [12, 345, 2, 6, 7896]
#     print(find_num(arr))