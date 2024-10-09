class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {}
        prefix[0] = -1

        cur_val = 0
        if len(nums) < 2:
            return False

        for i in range(len(nums)):
            cur_val += nums[i]
            if cur_val != 0 and cur_val % k == 0 and i >=1:
                return True
            break_point = prefix.get(cur_val % k, -2)
            if break_point == -2:
                prefix[cur_val % k] = i
                continue
            elif i - break_point > 1:
                return True
            else:
                continue

        return False