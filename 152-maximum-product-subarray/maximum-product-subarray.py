class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax = nums[0]
        curmin = nums[0]
        allmax = nums[0]
        print("pos", curmin, curmax, allmax)

        for i in range(1, len(nums)):
            if nums[i] == 0:
                curmax = 0
                curmin = 0
                allmax = max(allmax, 0)
            else:
                oldcurmax = curmax
                curmax = max(nums[i], curmax * nums[i], curmin * nums[i])
                curmin = min(nums[i], curmin * nums[i], oldcurmax * nums[i])

                allmax = max(allmax, curmax)
            print("pos", curmin, curmax, allmax)
            
        
        return allmax



        