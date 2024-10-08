class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # right = m + n - 1
        # idx1 = m - 1
        # idx2 = n - 1

        # if len(nums2) == 0:
        #     return
        

        # while idx1 >= 0:
        #     if idx2 < 0 or (idx1 >= 0 and nums1[idx1] > nums2[idx2]):
        #         nums1[right] = nums1[idx1]
        #         idx1 -= 1
        #     else:
        #         print(idx2)
        #         nums1[right] = nums2[idx2]
        #         idx2 -= 1

        #     right -= 1
        midx = m - 1
        nidx = n - 1 
        right = m + n - 1

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1

            right -= 1
        