class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = nums[0]
        i = 1
        length = len(nums)
        c = 0
        while i < length:
            if cur == nums[i]:
                nums.pop(i)
                length -= 1
            else:
                cur = nums[i]
                i += 1
                c += 1

        return c + 1