'''
Pangram là một chuỗi, trong đó tất cả các ký tự chữ cái xuất hiện ít nhất 1 lần.

Cho chuỗi sentence chứa các ký tự chữ cái tiếng Anh viết thường.
Hãy viết chương trình xác định xem chuỗi đã cho có phải là một chuỗi pangram hay không.
Đầu ra hiển thị true nếu chuỗi sentence là chuỗi pangram, hoặc ngược lại, đầu ra hiển thị false.
'''

class Solution:
    def pangram(self, s):
        seen = set()
        for x in s:
            if x in seen:
                return False
            seen.add(x)
        return True

if __name__ == '__main__':
    s = "thequi"
    vd3 = Solution()
    print(vd3.pangram(s))

