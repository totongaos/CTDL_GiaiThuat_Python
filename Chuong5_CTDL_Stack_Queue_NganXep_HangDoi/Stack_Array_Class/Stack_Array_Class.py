# Stack implementation in python
class MyStack:
    #00 Creating a stack
    def __init__(self, size):
        self.size = size
        self.stack = [None]*size
        self.top_index = -1
    #00 isFull
    def isFull(self):
        return self.top_index == (self.size - 1)
    #00 isEmpty
    def isEmpty(self):
        return self.top_index < 0

    #Adding items into the stack
    def push(self, item):
        if self.isFull():
            return "Stack is Full !!!"
        self.top_index += 1
        self.stack[self.top_index] = item
        return item

    #Removing an element from the stack
    def pop(self):
        if self.isEmpty(): #check empty stack
            return "Stack is empty!!!"
        item = self.stack[self.top_index]
        self.stack[self.top_index] = None
        self.top_index -= 1
        return item

    # Return the top from stack without removing it
    def peek(self):
        if self.isEmpty():  # check empty stack
            return "Stack is empty!!!"
        return self.stack[self.top_index]

    #Trong Stack_linkedList chỉ có thể show từ ngược vì LIFO
    def display(self):
        if self.isEmpty():
            print("Stack is empty!!!", end="\n\n")
        else:
            print("All elements in Stack:", end=" ")
            for i in reversed(range(0, self.top_index + 1)):
                print(self.stack[i], end=" ")
            print("\n")