class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        n = len(nums)
        res = []
        cur = []
        taken = [False] * len(nums)
        taken_count = 0
        def backtrack():
            nonlocal taken_count
            if taken_count == n:
                res.append(cur.copy())
                return
            for i in range(n):
                if not taken[i]:
                    taken[i] = True
                    cur.append(nums[i])
                    taken_count += 1
                    backtrack()

                    taken[i] = False
                    taken_count -= 1
                    cur.pop()

        backtrack()
        return res
            
