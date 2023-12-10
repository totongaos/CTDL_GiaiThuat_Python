if __name__ == '__main__':
    myMap = {}

    myMap[111] = "Tran Van A"
    myMap[222] = "Nguyen Van A"
    myMap[333] = "Ho Thi A"

    print("size: " + str(len(myMap)))
    for key in myMap:
        print(key , " : " , str(myMap[key]))