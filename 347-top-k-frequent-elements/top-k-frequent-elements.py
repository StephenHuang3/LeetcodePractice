import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        h = []
        for num, c in count.items():
            if len(h) < k:
                heapq.heappush(h, (c, num))
            else:
                heapq.heappushpop(h, (c, num))

        res = [f[1] for f in h]
        return res

        
        

