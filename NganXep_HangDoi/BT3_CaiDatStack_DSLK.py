# Python program for linked list implementation of stack
# Class to represent a node
class StackNode:
	# Constructor to initialize a node
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	# Constructor to initialize the root of linked list
	def __init__(self):
		self.root = None

	def isEmpty(self):
		return True if self.root is None else False

	def push(self, data):
		newNode = StackNode(data)
		newNode.next = self.root
		self.root = newNode
		# print ("% d pushed to stack" % (data))

	def pop(self):
		if (self.isEmpty()):
			return float("-inf")
		temp = self.root
		self.root = self.root.next
		popped = temp.data
		return popped

# Driver code
stack = Stack()

# n=int(input())
n = 5
for i in range(0,n):
	step = input().split()  #nhập giá trị của từng phần tử trong mảng
	if not step:
		break
	if 'push' in step:
		stack.push(step[1])
		# push(stack,step[1])
	elif 'pop' in step:
		stack.pop()
		# pop(stack)

count = 1
while True:
	tmp = stack.pop()
	if tmp != float("-inf"):
		print(tmp,end=" ")
		count = 2
	elif count ==1 :
		print("Stack is Empty!")
		break
	else: break