'''
Give arr string s containing just the characters '(', ')', '{', '}', '[', ']',
determine if the input string is valid
An input string is valid if:
    1. Open brackets must be closed by the same type of brackets
    2. Open brackets must be closed in the correct order

Ex 1: Input s = "()"  -> return True
Ex 2: Input s = "()[]"  -> return True
Ex 3: Input s = "(][)"  -> return False
Ex 4: Input s = "([])"  -> return True
'''
from  collections import deque

def valid_parentheses(s):
    tempOpen = ["(", "{", "["]
    myStack = deque()
    for i in range(0,len(s)):
        c = s[i]
        if c in tempOpen:
            myStack.append(c)
        else:
            if len(myStack) == 0:
                return False
            tempClose = myStack[-1]
            if (c == ")" and tempClose == "(") or  (c == "]" and tempClose =="[") or  (c == "}" and tempClose =="{"):
                myStack.pop()
            else:
                return False
    return True

if __name__ == '__main__':
    s = "([])"
    print(valid_parentheses(s))
