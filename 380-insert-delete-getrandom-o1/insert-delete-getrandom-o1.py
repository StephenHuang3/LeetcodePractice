import random
class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.hp = {}
        

    def insert(self, val: int) -> bool:
        if val in self.hp:
            return False
        
        self.lst.append(val)
        self.hp[val] = len(self.lst) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hp:
            return False
        
        pos = self.hp[val]
        self.lst[pos] = self.lst[-1]
        self.hp[self.lst[-1]] = pos
        self.lst.pop()
        del self.hp[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()