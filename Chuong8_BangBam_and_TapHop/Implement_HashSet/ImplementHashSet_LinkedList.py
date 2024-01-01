#2. class ListNode
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


#1. class HashSet main class
class HashSet:
    def __init__(self):
        self.key_space = 10**4
        self.set = [ListNode(0) for i in range(self.key_space)]

    def add(self, key):
        # index = key % self.key_space  #hash func
        curr = self.set[key % self.key_space]

        while curr.next:
            if curr.next.key == key:
                return key
            curr.next = curr
        curr.next = ListNode(key)
        return key

    def remove(self, key):
        curr = self.set[key % self.key_space]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return key
            curr.next = curr
        return key
    def contains(self, key):
        curr = self.set[key % self.key_space]

        while curr.next:
            if curr.next.key == key:
                return True
            curr.next = curr
        return False

    def display(self):
        print("all elements in set: ", end=" ")
        for i in self.set:
            if i.next != None:
                print(i.next.key, end=" ")
        print("\n")


#3. main
if __name__ == '__main__':

    ob = HashSet()

    print("add 500:",ob.add(505))
    print("add 50:",ob.add(55))
    print("add 6:",ob.add(25))
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