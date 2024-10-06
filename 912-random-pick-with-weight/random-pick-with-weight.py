import random
class Solution:

    def __init__(self, w: List[int]):
        self.sum = sum(w)
        self.lis = []
        c = 0
        
        for i in range(len(w)):
            self.lis.append(c + w[i])
            c += w[i]
        

    def pickIndex(self) -> int:
        random_number = random.randint(1, self.sum)
        return bisect_left(self.lis, random.randint(1, self.sum))
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()