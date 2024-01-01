#Design HashSet in Python

#2. checking the values and will return the output class
class Checkingvalues:
    #initialization func which has list mathfun
    def __init__(self):
        self.mathfun = []

    #update values func
    def update(self, key):
        found = False
        print(enumerate(self.mathfun))
        for i,k in enumerate(self.mathfun):
            # print(i,k)
            if key == k:
                self.mathfun[i] = key
                found = True
                break

        if not found:
            self.mathfun.append(key)

    #get values functions
    def get(self, key):
        for k in self.mathfun:
            if k == key:
                return True
        return False

    #remove values func
    def remove(self, key):
        for i,k in enumerate(self.mathfun):
            if key == k:
                del self.mathfun[i]


#1. class HashSet main class
class HashSet:
    def __init__(self) -> object:
        self.key_space = 10000
        self.hash_table = [Checkingvalues()  for i in range(self.key_space)]

    def hash_val(self, key):
        hash_key = key % self.key_space
        return hash_key

    #add func
    def add(self, key):
        self.hash_table[self.hash_val(key)].update(key)
        return self.hash_val(key)

    #remove func
    def remove(self, key):
        self.hash_table[self.hash_val(key)].remove(key)
        return self.hash_val(key)

    #contains func
    def contains(self, key):
        return self.hash_table[self.hash_val(key)].get(key)

    def display(self):
        lst=[]
        for i in self.hash_table:
            # print(self.hash_table)
            if len(i.mathfun) != 0:
                # print(i.mathfun)
                lst.append(i.mathfun[0])
        print(lst)

