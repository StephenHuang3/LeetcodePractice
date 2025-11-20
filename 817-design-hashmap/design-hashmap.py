class MyHashMap:

    def __init__(self):
        self.map = [[] for _ in range(1000)]

    def hash(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        pos = self.hash(key)
        for i in self.map[pos]:
            print(i)
        self.map[pos] = [i for i in self.map[pos] if i[0] != key]
        self.map[pos].append((key, value))
        

    def get(self, key: int) -> int:
        pos = self.hash(key)

        for check_key, val in self.map[pos]:
            if check_key == key:
                return val

        return -1

    def remove(self, key: int) -> None:
        pos = self.hash(key)

        self.map[pos] = [i for i in self.map[pos] if i[0] != key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)