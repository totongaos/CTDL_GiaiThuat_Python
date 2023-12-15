class MyHashSet:
    def __init__(self):
        self.myBuckets = {}
        self.size = 1000

    #Return hash value
    def hashFuntion(self, key):
        return key % self.size
    def add(self, key):
        hash_val_index = MyHashSet.hashFuntion(key)
        bucket = self.myBuckets[hash_val_index]
        key_index = bucket.
    def remove(self, key):
    def contains(self, key):

