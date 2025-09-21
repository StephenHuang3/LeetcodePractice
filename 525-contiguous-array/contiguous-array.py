class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cur_sum = 0
        first_sum = {}
        max_len = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                cur_sum -= 1
            else:
                cur_sum += nums[i]
            
            if cur_sum == 0:
                max_len = i + 1
                continue
            
            if cur_sum not in first_sum:
                    first_sum[cur_sum] = i
            
            if cur_sum in first_sum:
                # print("i, first_sum[-cur_sum],", i, first_sum[-cur_sum])
                max_len = max(max_len, i - first_sum[cur_sum])

            # print(max_len)

        print(first_sum)
        return max_len