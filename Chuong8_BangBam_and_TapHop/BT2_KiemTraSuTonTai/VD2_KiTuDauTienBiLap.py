'''
Cho chuỗi s. Trả về ký tự đầu tiên bị lặp (giả sử input có ít nhất 1 ký tự trùng lặp).
'''

class Solution:
    def repeatedCharacter(self, s):
        seen = set()
        for i in range(len(s)):
            #lay tung p.tu trong s có trong dict ko?
            c = s[i]
            if c in seen:
                return c
            seen.add(c)
        return "Sorry I couldn't find it !!!"

if __name__ == '__main__':
    s = "tek4vietnam"
    vd2 = Solution()
    print(vd2.repeatedCharacter(s))

