'''
Cài đặt class RecentCounter. Class này có phương thức ping (int t) để ghi lại một lượt gọi tại thời điểm t.

Trả về một số nguyên đại diện cho số lượng các lượt gọi đã xảy ra trong khoảng thời gian [t - 3000, t].
Các lượt gọi sẽ có thời gian ngày càng tăng.
'''
from  collections import deque
class RecentCounter:
    def __init__(self):
        self.queue = deque()
    def ping(self,t):
        self.queue.append(t)
        while (self.queue[0] < (t-3000)) and self.queue:
            self.queue.popleft()
        return len(self.queue)

    def display(self):
        print(self.queue)
if __name__ == '__main__':
    myQueue = RecentCounter()
    temp = [0,1,100,3001,3002,4000,6000]
    for t in temp:
        print(myQueue.ping(t))
    myQueue.display()

