class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class MyLinkedListStack:
    def __init__(self):
        self.topNode = Node
        self.topNode = None

    def isEmpty(self):
        return self.topNode == None
    def isFull(self):
        return False

    def push(self, value):
        #them vao dau p.tu cua linked list
        if self.isFull() == False:
            new_node = Node(value)
            new_node.next = self.topNode
            self.topNode = new_node
            return value
        return "Stack is Full !!!"
    def pop(self):
        #them vao dau p.tu cua linked list
        if self.isEmpty() == False:
            value = self.topNode
            self.topNode = self.topNode.next
            return value.data
        return "Stack is Empty !!!"


    #Trong Stack_linkedList chỉ có thể show từ ngược vì LIFO
    def display(self):
        if self.isEmpty():
            print("All elements in Stack: Stack is empty!!!", end="\n\n")
        else:
            value = self.topNode
            print("All elements in Stack:", end=" ")
            while value:
                print(value.data, end=" ")
                value = value.next
            print("\n")

