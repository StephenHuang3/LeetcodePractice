import random

class RandomizedSet:

    def __init__(self):
        self.hp = {}
        self.lis = []

    def insert(self, val: int) -> bool:
        if val in self.hp:
            return False
        self.hp[val] = len(self.lis)
        self.lis.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hp:
            return False
        val_pos = self.hp[val]
        if val_pos != len(self.lis) - 1:
            exchange_element = self.lis[-1]
            self.lis[val_pos], self.lis[-1] = self.lis[-1], self.lis[val_pos]
            self.hp[exchange_element] = val_pos

        self.lis.pop()
        del self.hp[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lis)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()