class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sample = []
        def back(pos):
            if pos == len(nums):
                res.append(sample.copy())
                return
            back(pos + 1)
            sample.append(nums[pos])
            back(pos + 1)
            sample.pop()
            return


        back(0)
        return res