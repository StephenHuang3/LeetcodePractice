class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[j] or nums[i] == nums[j] and (j - 1 < 0 or nums[j] != nums[j - 1]):
                j += 1
                nums[j] = nums[i]

        return j + 1
        
# 1 1 2 2 3 3 4 4 4
#       j
#       i

# 1 1 2 2 3 3 4 4