class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {}
        count[0] = 1
        cur_sum = 0
        res = 0

        for n in nums:
            cur_sum += n
            need = cur_sum - k
            if need in count:
                res += count[need]
            if cur_sum not in count:
                count[cur_sum] = 0
            count[cur_sum] += 1
        return res