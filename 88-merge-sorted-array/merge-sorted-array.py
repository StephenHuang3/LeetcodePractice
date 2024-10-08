class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        right = m + n - 1
        idx1 = m - 1
        idx2 = n - 1

        if len(nums2) == 0:
            return
        

        while idx2 >= 0:
            if idx1 >= 0 and nums1[idx1] > nums2[idx2]:
                nums1[right] = nums1[idx1]
                idx1 -= 1
            else:
                print(idx2)
                nums1[right] = nums2[idx2]
                idx2 -= 1

            right -= 1
        