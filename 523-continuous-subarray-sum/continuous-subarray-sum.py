class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {}
        prefix[0] = -1

        cur_val_mod = 0

        for i in range(len(nums)):
            cur_val_mod = (cur_val_mod + nums[i]) % k
            if cur_val_mod in prefix:
                if i - prefix[cur_val_mod] > 1:
                    return True
                continue
            else:
                prefix[cur_val_mod] = i

        return False
