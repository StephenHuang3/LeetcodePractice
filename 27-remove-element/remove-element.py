class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                nums.pop(i)
                length -= 1
                print(nums)
            else:
                i += 1
                c += 1

        return c
        