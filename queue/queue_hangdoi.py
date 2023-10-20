# Queue implementation in Python
class Queue:
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

def check_Prime(a):
    for i in range(2, (a // 2) + 1):
        if a % i == 0:
            return False
    if a > 1: return True
    return False

n = 1000
q = Queue()
j = 0
for i in range(2,10):
    if check_Prime(i):
        q.enqueue(i)

#cach 1
while q.size() !=0:
    for e in [1, 3, 7, 9]:
        j =q.queue[0]*10+e
        if j<n and check_Prime(j):
            q.enqueue(j)
    print(q.dequeue(),end=" ")

#cach 2
# for i in q.queue:
#     if i*10 > (n - 1):
#         break
#     for e in [1, 3, 7, 9]:
#         j = i*10+e
#         if j > (n-1):
#             break
#         elif check_Prime(j):
#             q.enqueue(j)
# print(*q.queue)
