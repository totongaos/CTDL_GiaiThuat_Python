from sampleSetting import *

def main():
    #khai báo lst là class Linked List
    L1 = LinkedList()
    n = 3

    #a - add value
    print('a: add value-------')
    for i in range(n):
        L1.add_Value(str(input()))
    L1.print_List()


    #b - insert value
    print("b: chen value ----------")
    index_k = 1
    numX = 10
    print(f'chen {numX} vao vi tri {index_k}')
    L1.insert_Value(index_k,numX)
    L1.print_List()

    #c - find value

    #d - delete value

    #e - update value

    #f - delete all


if __name__ == '__main__':
    main()