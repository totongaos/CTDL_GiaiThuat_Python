'''Ví dụ 4: Chìa khóa và Phòng
Có n phòng được đánh số từ 0 đến n - 1 và tất cả các phòng đều bị khóa ngoại trừ phòng 0.
Mục tiêu của bạn là đi vào tất cả các phòng. Khi vào một căn phòng,
bạn có thể tìm thấy một bộ chìa khóa riêng biệt trong đó.
Mỗi chìa khóa có một số cho biết nó mở khóa phòng nào và bạn có thể mang theo tất cả chúng để mở khóa các phòng khác.
Cho mảng rooms trong đó rooms[i] là tập hợp các khóa mà bạn có thể lấy được nếu đã vào phòng i,

trả về true nếu bạn có thể đi vào tất cả các phòng hoặc ngược lại trả về false.
'''

class Solution:
    def canVisitAllRooms(self,rooms: list[list[int]]) -> int:
        def dfs(node):
            # 4.2.1 xai for check peak con của peak vua duyet
            for peak in rooms[node]:
                if peak not in seen: #neu chua ở trong stack thì them vào
                    seen.append(peak)
                    dfs(peak) #dequy den khi het dinh con

        seen = [0]
        dfs(0)
        print(seen)
        return len(seen) == len(rooms)


#3. Ham main
if __name__ == '__main__':
    # rooms = defaultdict(list)
    rooms = {0: [1, 3, 9], 1: [2, 5],
             2: [], 3: [7], 4: [], 5: [],
             6: [], 7: [], 8: [], 9: [4, 6, 8]}
    # print(rooms)

    print(Solution.canVisitAllRooms(Solution, rooms))

'''
{0: [1, 3, 9], 1: [0, 3], 3: [1, 2], 2: [3], 5: [0, 4], 4: [5, 6], 6: [4]}) 
'''