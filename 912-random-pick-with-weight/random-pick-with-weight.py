import random
class Solution:

    def __init__(self, w: List[int]):
        self.sum = sum(w)
        self.lis = w
        

    def pickIndex(self) -> int:
        random_number = random.randint(1, self.sum)
        for i in range(len(self.lis)):
            random_number -= self.lis[i]
            if random_number <= 0:
                return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()