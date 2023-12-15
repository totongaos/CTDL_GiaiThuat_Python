from  collections import deque
if __name__ == '__main__':
    #Tao 1 Queue kieu int
    myQueue = deque()

    #2. add cac value vao Queue moi tao
    myQueue.append(1)
    myQueue.append(2)
    myQueue.append(3)

    print("myQueue:", end=" ")
    while len(myQueue)>0:
        print(myQueue[0], end=" ") #ktra p.tu dau cua Queue la value nao
        myQueue.popleft() #loai bo p.tu dau
