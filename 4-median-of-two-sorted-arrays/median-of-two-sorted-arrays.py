class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        l = 0
        r = len(nums1) - 1
        half = (len(nums1) + len(nums2)) // 2

        while True:
            last_left_idx = (l + r) // 2
            last_left_idx2 = half - last_left_idx - 2
            print(last_left_idx)
            print(last_left_idx2)

            most_left = nums1[last_left_idx] if last_left_idx >= 0 else float("-inf")
            most_left2 = nums2[last_left_idx2] if last_left_idx2 >= 0 else float("-inf")
            least_right = nums1[last_left_idx + 1] if last_left_idx + 1 < len(nums1) else float("inf")
            least_right2 = nums2[last_left_idx2 + 1] if last_left_idx2 + 1 < len(nums2) else float("inf")

            if most_left <= least_right2 and most_left2 <= least_right:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(most_left, most_left2) + min(least_right, least_right2)) / 2
                else:
                    return  min(least_right, least_right2)

            if most_left > least_right2:
                r = last_left_idx - 1
            else:
                l = last_left_idx + 1
