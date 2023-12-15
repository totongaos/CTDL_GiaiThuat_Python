# Cho hai chuỗi s và t, trả về true nếu s là một dãy con của t, ngược lại trả về false.

class Solution:
    def array_OfTwoPoint(self,string_s,string_t):
        index1 = index2 = 0

        while index1 < len(string_s) and index2 < len(string_t):
            if string_s[index1] == string_t[index2]:
                index1 += 1
            index2 += 1

        return index1 == len(string_s)

    # print(array_OfTwoPoint(string_s,string_t))
c = Solution
print(c.array_OfTwoPoint('','asd','gasdkkk'))