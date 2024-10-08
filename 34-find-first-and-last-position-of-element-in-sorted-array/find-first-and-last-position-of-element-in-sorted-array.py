from bisect import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        min_value = bisect_left(nums, target)
        max_value = bisect_right(nums, target)

        if min_value == max_value:
            return [-1,-1]

        return [min_value, max_value - 1]