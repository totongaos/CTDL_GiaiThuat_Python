'''
Give an encoded string, return its decoded string.
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
'''
from  collections import deque
class DecodeString:
    def __init__(self):
        self.stack = deque()
    def solution(self,s):
        for i in range(0, len(s)):
            c =s[i]
            if c == ']':
                #Pop until meet '['
                temp_s = ""
                while self.stack[-1] != '[':
                    temp_s = self.stack[-1] + temp_s
                    self.stack.pop()
                #Remove "["
                self.stack.pop()

                #Get num
                num_str1 = ''
                while len(self.stack) != 0 and self.stack[-1].isdigit():
                    num_str1 = self.stack.pop() + num_str1
                num_int = int(num_str1)

                #Repeat the string
                loop_str = num_int*temp_s

                #Add the result back to stack
                for j in range(0,len(loop_str)):
                    self.stack.append(loop_str[j])

            else:
                self.stack.append(c)

        res = ''
        while len(self.stack) !=0:
            res = self.stack.pop() + res
        return res


if __name__ == '__main__':
    s = "3[ab2[du]]"
    stack = DecodeString()
    print(stack.solution(s))


