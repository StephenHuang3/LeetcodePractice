class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def merge(l1, l2):
            new = []
            c1 = 0
            c2 = 0
            while c1 < len(l1) and c2 < len(l2):
                if l1[c1] + l2[c2] > l2[c2] + l1[c1]:
                    new.append(l1[c1])
                    c1 += 1
                else:
                    new.append(l2[c2])
                    c2 += 1

            if c1 < len(l1):
                new += l1[c1:]
            elif c2 < len(l2):
                new += l2[c2:]
            return new

        def mergesort(lis):
            if len(lis) <= 1:
                return lis
            n = len(lis) // 2
            left = mergesort(lis[:n])
            right = mergesort(lis[n:])

            return merge(left, right)

        nums = mergesort([str(x) for x in nums])
        if nums[0] == '0':
            return '0'

        return "".join(nums)