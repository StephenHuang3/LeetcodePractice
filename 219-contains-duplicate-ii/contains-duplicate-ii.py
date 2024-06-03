class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup = {}
        for i, num in enumerate(nums):
            if num not in dup:
                dup[num] = i
            elif i - dup[num] <= k:
                return True
            else:
                dup[num] = i

        return False