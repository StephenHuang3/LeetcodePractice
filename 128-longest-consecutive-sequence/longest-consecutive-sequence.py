class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hp = set()
        max_length = 0
        for num in nums:
            hp.add(num)

        for num in hp:
            cur_len = 1
            if num + 1 not in hp:
                cur_val = num
                while cur_val - 1 in hp:
                    cur_len += 1
                    cur_val -= 1
            
            max_length = max(max_length, cur_len)

        return max_length