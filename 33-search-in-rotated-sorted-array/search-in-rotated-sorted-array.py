class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            # print("cur m", nums[m])
            if nums[m] == target:
                return m
            # print(nums[l], nums[r], nums[m])

            if nums[l] <= nums[m] <= nums[r]:
                if target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[r] <= nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] <= nums[r] <= nums[l]:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1            
            
        
        if nums[l] == target:
            return l
        return -1
            