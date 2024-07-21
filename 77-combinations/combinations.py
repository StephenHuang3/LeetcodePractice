class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []
        def findall(at):
            if len(comb) == k:
                res.append(comb[:])
                return
            
            for num in range(at, n + 1):
                comb.append(num)
                findall(num + 1)
                comb.pop()
        
        findall(1)
        return res
        
        