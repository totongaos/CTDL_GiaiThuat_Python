string_1st = [x for x in input().split()]
# string_1st = 't e k 4'
# string_1st = list(string_1st)

def array_OfTwoPoint(string_1st):
    left = 0
    right = len(string_1st) - 1
    while left < right:
        string_1st[left],string_1st[right] = string_1st[right],string_1st[left]
        right -= 1
        left += 1
    return string_1st

print(*array_OfTwoPoint(string_1st))