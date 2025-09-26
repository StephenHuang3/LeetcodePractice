class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def dfs(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    a, b = nums[i], nums[j]
                    cand = [a + b, a - b, b - a, a * b,]
                    if abs(b) > EPS:
                        cand.append(a / b)
                    if abs(a) > EPS:
                        cand.append(b / a)
                    
                    for val in cand:
                        if dfs(next_nums + [val]):
                            return True

            return False

        
        return dfs([float(x) for x in cards])