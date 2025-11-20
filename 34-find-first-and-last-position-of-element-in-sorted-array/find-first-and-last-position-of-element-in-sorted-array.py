import bisect


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]

        if target < nums[0] or nums[-1] < target:
            return [-1, -1]

        left = bisect.bisect_left(nums, target)
        if nums[left] != target:
            return [-1, -1]
        right = bisect.bisect_right(nums, target)

        return [left, max(left, right - 1)]