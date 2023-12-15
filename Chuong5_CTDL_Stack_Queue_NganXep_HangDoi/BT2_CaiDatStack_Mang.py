# Stack implementation in python

# Creating a stack
def create_stack():
    stack = []
    return stack

# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0

# Adding items into the stack
def push(stack, item):
    return stack.append(item)

# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        result.append(-1)
        return
    result.append(stack.pop())
    return

if __name__ == '__main__':
    stack = create_stack()
    result = []
    # n=int(input())
    n = 5
    for i in range(0,n):
        step = input().split() #nhập giá trị của từng phần tử trong mảng
        if not step:
            break
        if 'push' in step:
            push(stack,step[1])
        elif 'pop' in step:
            pop(stack)

    print(*result)