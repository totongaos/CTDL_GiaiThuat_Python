from  collections import deque
if __name__ == '__main__':
    #Tao 1 stack kieu int
    myStack = deque()

    #2. add cac value vao stack moi tao
    myStack.append(1)
    myStack.append(2)
    myStack.append(3)

    print("myStack:", end=" ")
    while len(myStack)>0:
        print(myStack[-1], end=" ") #ktra p.tu cuoi cua stack la value nao
        myStack.pop() #loai bo p.tu cuoi