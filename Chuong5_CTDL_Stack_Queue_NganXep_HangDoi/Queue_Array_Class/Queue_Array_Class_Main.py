from Chuong5_CTDL_Stack_Queue_NganXep_HangDoi.Queue_Array_Class.Queue_Array_Class import MyQueue
if __name__ == '__main__':
    queue = MyQueue(4)

    print(f"popped item: {queue.pop()}")
    print('count:', queue.count())
    queue.display()

    print(f'push item: {queue.push(str(1))}')
    print(f'push item: {queue.push(str(2))}')
    print(f'push item: {queue.push(str(3))}')
    print('count:', queue.count())
    queue.display()


    print(f"popped item: {queue.pop()}")
    print(f"popped item: {queue.pop()}")
    print(f"popped item: {queue.pop()}")


    print('count:', queue.count())
    queue.display()
