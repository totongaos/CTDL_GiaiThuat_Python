'''
Cho DS cạnh → chuyển sang Ma trận kề tương ứng
'''

if __name__ == '__main__':
    n = int(input("nhap so luong dinh: "))
    m = int(input("nhap so luong canh: "))

    a = [[0]*(m+1) for i in range(m+1)]
    # print(a)

    # Duyet m canh ->  nhap 2 đinh của canh
    for i in range(m):
        #input DS Canh
        x, y = [int(z) for z in input().split()]
        # Tao Matrix ke
        a[x][y] = a[y][x] = 1
    print(a)
    #In matran ke tuong ung adjacency_matrix
    for row in range(n):
        for col in range(n):
            print(a[row][col],end=" ")
        print("", end="\n")