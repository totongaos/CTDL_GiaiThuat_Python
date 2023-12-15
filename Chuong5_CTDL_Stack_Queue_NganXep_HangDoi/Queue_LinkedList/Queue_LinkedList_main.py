from Chuong5_CTDL_Stack_Queue_NganXep_HangDoi.Queue_LinkedList.Queue_LinkedList import MyLinkedListQueue

if __name__ == '__main__':
    q = MyLinkedListQueue()
    print(f"push item: {q.push(2)}")
    # print(f"push item: {q.push(3)}")
    # print(f"push item: {q.push(4)}")
    q.display()

    print(f"pop item: {q.pop()}")
    print(f"pop item: {q.pop()}")
    q.display()
