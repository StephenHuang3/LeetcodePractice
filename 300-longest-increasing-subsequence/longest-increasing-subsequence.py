class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]

        def insertDP(num):
            l = 0
            r = len(dp) - 1

            while l < r:
                m = (l + r) // 2                
                if dp[m] < num:
                    l = m + 1
                else:
                    r = m

            dp[l] = num

        
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                insertDP(nums[i])

        return len(dp)