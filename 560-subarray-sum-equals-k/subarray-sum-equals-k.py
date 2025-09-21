from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = defaultdict(int)
        pref[0] = 1
        total = 0
        count = 0

        for num in nums:
            total += num

            if total - k in pref:
                count += pref[total - k]

            pref[total] = pref.get(total, 0) + 1

        return count