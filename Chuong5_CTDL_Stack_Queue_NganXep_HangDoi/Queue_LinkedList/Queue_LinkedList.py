class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class MyLinkedListQueue:
    def __init__(self):
        self.head = Node(None)
        self.head = None
        self.tail = Node(None)
        self.tail = None

    def isEmpty(self):
        return self.head == None and self.tail == None

    def isFull(self):
        return False

    def push(self, value):
        if self.isFull():
            return "Queue is Full !!!"
        else:
            new_node = Node(value)
            if self.isEmpty():
                self.head = self.tail = new_node
                return value
            else:
                self.tail.next = new_node
                self.tail = new_node
                return value

    def pop(self):
        if self.isEmpty():
            return "Queue is Empty !!!"
        else:
            value = self.head.data
            if self.tail == self.head:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            return value

    def display(self):
        if self.isEmpty():
            print("All elements in Stack: Stack is empty!!!", end="\n\n")
            return
        value = self.head
        print("All elements in Stack:", end=" ")
        while value:
            print(value.data, end=" ")
            value = value.next
        print("\n")
