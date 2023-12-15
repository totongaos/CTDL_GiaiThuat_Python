# Stack implementation in python
class MyQueue:
    #00 Creating a stack
    def __init__(self, size):
        self.size = size
        self.queue = [None]*size
        self.head_index = -1
        self.tail_index = -1
    #00 isFull
    def isFull(self):
        return self.tail_index == (self.size - 1)
    #00 isEmpty
    def isEmpty(self):
        return self.head_index == -1 and self.tail_index == -1

    #Adding items into the stack
    def push(self, item):
        if self.isFull() == False:
            if self.isEmpty(): #rỗng phải tăng head lên 1 để tý pop
                self.head_index +=1
            self.tail_index += 1
            self.queue[self.tail_index] = item
            return item
        return "Queue is Full !!!"
    #count số ptu
    def count(self):
        if self.isEmpty():
            return 0
        return self.tail_index - self.head_index + 1


    # Removing an element from the stack
    def pop(self):
        if self.isEmpty() == False:  # check empty stack
            value = self.queue[self.head_index]
            self.head_index += 1
            if self.head_index > self.tail_index: #-> fix bug khi len(array) == 1
                self.head_index = self.tail_index = -1
            return value
        return "Queue is empty!!!"
    # Return the top from stack without removing it
    def peek(self):
        if self.isEmpty():  # check empty stack
            return "Queue is empty!!!"
        return self.queue[self.top_index]

    #print all elements in Stack
    def display(self):
        if self.isEmpty():
            print("All elements in Queue: Queue is empty!!!", end="\n\n")
        else:
            print("All elements in Queue:", end=" ")
            for i in range(self.head_index, self.tail_index+1):
                print(self.queue[i], end=" ")
            print("\n")
