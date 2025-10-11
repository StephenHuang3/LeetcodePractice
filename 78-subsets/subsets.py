class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []

        def backtrack(pos):
            if pos == len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[pos])
            backtrack(pos + 1)
            cur.pop()
            backtrack(pos + 1)

        backtrack(0)
        return res