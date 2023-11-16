'''**Thuật toán đệ quy**

- Di chuyển n-1 đĩa trên cùng từ cọc nguồn sang cọc trung gian.
- Di chuyển đĩa thứ n từ cọc nguồn đến cọc đích.
- Di chuyển n-1 đĩa từ cọc trung gian sang cọc đích, sử dụng cọc nguồn làm trung gian.
- Trường hợp cơ bản của đệ quy là khi chỉ có một đĩa để di chuyển. Trong trường hợp này, chúng ta chỉ cần di chuyển đĩa từ cọc nguồn đến cọc đích.
'''


#hàm tháp HN
def towerOfHanoi(n,from_rod,to_rod,aux_rod):
    if n==1: #1. check nếu n ==1 thì print & return
        print(f'Disk {n} moved from {from_rod} to {to_rod}')
        return
    #2. nếu n >1 thì dequy n-1, đổi vị trí cột đích và trung gian. mỗi lần dequy sẽ doi cho 1 lan
    towerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    #3. sau khi dequy xong thì print cột gốc và đích ứng với n
    print(f'Disk {n} moved from {from_rod} to {to_rod}')
    #4. dequy thêm lần nữa và đổi vị trí cột gốc và trung gian
    towerOfHanoi(n-1,aux_rod, to_rod , from_rod)


#1. ban đầu truyền C làm cột đích, vì n=1 sẽ từ a -> C
towerOfHanoi(3,'A','C','B')
