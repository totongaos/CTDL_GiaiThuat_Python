from Chuong5_CTDL_Stack_Queue_NganXep_HangDoi.Stack_LinkedList.Stack_LinkedList import MyLinkedListStack

if __name__ == '__main__':
    stack = MyLinkedListStack()
    print(f"push item: {stack.push(2)}")
    print(f"push item: {stack.push(3)}")
    print(f"push item: {stack.push(4)}")
    stack.display()
    print(f"pop item: {stack.pop()}")
    print(f"pop item: {stack.pop()}")
    print(f"pop item: {stack.pop()}")
    print(f"pop item: {stack.pop()}")

    stack.display()