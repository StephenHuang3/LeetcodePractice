class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        def backtrack():
            if len(nums) == 0:
                res.append(perm[:])
                return
            
            for i in range(len(nums)):
                rmv = nums.pop(i)
                perm.append(rmv)
                backtrack()
                perm.pop()
                nums.insert(i, rmv)

        backtrack()
        return res