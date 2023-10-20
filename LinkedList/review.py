class Node: #khai báo Node
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addValue(self, value):
        node_new = Node(value)
        if self.head == None:
            self.head = value
            self.tail = value
        else:
            self.tail = node_new
            self.tail.next = value


    def printValue(self):
        printVal = self.head
        print(printVal)

# Code execution starts here
if __name__ == '__main__':
    lst = LinkedList()
    lst.addValue(11)
    lst.addValue(12)
    lst.printValue()