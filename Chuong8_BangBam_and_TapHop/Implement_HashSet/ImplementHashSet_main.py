from Chuong8_BangBam_and_TapHop.Implement_HashSet.ImplementHashSet import HashSet
#3. main
if __name__ == '__main__':

    ob = HashSet()

    print("add 500:",ob.add(505))
    # print("add 50:",ob.add(55))
    # print("add 6:",ob.add(25))
    ob.display()
    print("contains 500000", ob.contains(5000))
    print("contains 10", ob.contains(10))

    print("add 2:", ob.add(2))

    print("add 6:", ob.add(6))
    print("add 2:", ob.add(2))
    ob.display()

    print("remove 3:", ob.remove(3))
    ob.display()
    print("contains 2", ob.contains(2))
    print("contains 3", ob.contains(3))