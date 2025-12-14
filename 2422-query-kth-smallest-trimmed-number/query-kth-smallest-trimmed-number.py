import heapq


class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        num_len = len(nums[0])
        ret = []

        for k, trim in queries:
            trimmed = [int(i[num_len - trim:]) for i in nums]
            hp = []
            for i, num in enumerate(trimmed):
                heapq.heappush(hp, (-num, -i))
                if len(hp) > k:
                    heapq.heappop(hp)

            # print(hp)
            neg_kth_smallest, neg_idx = heapq.heappop(hp)
            ret.append(-neg_idx)

        return ret