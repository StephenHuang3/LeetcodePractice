class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        c1 = 0
        c2 = 0
        output = []
        
        while c1 < m and c2 < n:
            if nums1[c1] < nums2[c2]:
                output.append(nums1[c1])
                c1 += 1
            else:
                output.append(nums2[c2])
                c2 += 1
            
        print(output)
        if c1 < m:
            output = output + nums1[c1:m]
        if c2 < n:
            output = output + nums2[c2:]

        for i in range(len(output)):
            nums1[i] = output[i]
        """
        Do not return anything, modify nums1 in-place instead.
        """
        