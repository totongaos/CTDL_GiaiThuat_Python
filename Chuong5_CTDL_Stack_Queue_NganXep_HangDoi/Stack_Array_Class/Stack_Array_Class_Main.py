from Chuong5_CTDL_Stack_Queue_NganXep_HangDoi.Stack_Array_Class.Stack_Array_Class import MyStack
if __name__ == '__main__':
    stack = MyStack(4)
    stack.display()

    print(f'push item: {stack.push(str(1))}')
    print(f'push item: {stack.push(str(2))}')
    print(f'push item: {stack.push(str(3))}')
    print(f'push item: {stack.push(str(5))}')
    stack.display()


    print(f"popped item: {stack.pop()}")
    stack.display()
    print(f"popped item: {stack.pop()}")
    stack.display()
    print(f"peek item: {stack.peek()}")

    stack.display()