class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = set()

        total = sum(nums)

        if total % 2 == 1:
            return False

        half = total // 2

        for num in nums:
            newset = set()
            for s in sums:
                newset.add(s + num)
            sums = sums | newset
            sums.add(num)
        
        if half in sums:
            return True

        print(sums)

        return False