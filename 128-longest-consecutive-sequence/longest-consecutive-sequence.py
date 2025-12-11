class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_len = 1
        nums_set = set(nums)

        for num in nums_set:
            if (num - 1) not in nums_set:
                seq = 1
                while (num + seq) in nums_set:
                    seq += 1

                max_len = max(max_len, seq)

        return max_len