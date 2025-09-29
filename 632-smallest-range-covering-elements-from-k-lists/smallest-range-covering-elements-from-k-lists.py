class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # have a heap(num, idx, which arr)
        hp = []
        max_val = float("-inf")
        cur_max_val = float("-inf")

        for i in range(len(nums)):
            heapq.heappush(hp, (nums[i][0], 0, i))
            max_val = max(max_val, nums[i][0])

        min_val = hp[0][0]
        cur_max_val = max_val

        while True:
            val, idx, arr_idx = heapq.heappop(hp)
            if len(nums[arr_idx]) == idx + 1:
                break
            heapq.heappush(hp, (nums[arr_idx][idx + 1], idx + 1, arr_idx))
            cur_max_val = max(nums[arr_idx][idx + 1], cur_max_val)
            cur_min_val = hp[0][0]

            if max_val - min_val > cur_max_val - cur_min_val:
                max_val = cur_max_val
                min_val = cur_min_val
        
        return [min_val, max_val]
