class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref = 1
        suf = 1
        allmax = float('-infinity')

        n = len(nums) - 1

        for i in range(n + 1):
            if pref == 0:
                pref = 1
            if suf == 0:
                suf = 1
            pref *= nums[i]
            suf *= nums[n - i]

            allmax = max(allmax, pref, suf)

        return allmax
            
        
        return allmax



        