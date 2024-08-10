class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        retmax = nums[0][0]

        for i in range(len(nums)):
            nums[i].sort()
            heapq.heappush(heap, (nums[i][0], i, 0))
            retmax = max(retmax, nums[i][0])
        
        retmin = heap[0][0]
        curmin = retmin
        curmax = retmax
        curminrange = retmax - retmin

        while len(heap) > 0:
            num, row, idx = heapq.heappop(heap)
            
            if idx + 1 == len(nums[row]):
                break
            heapq.heappush(heap, (nums[row][idx + 1], row, idx + 1))
            if nums[row][idx + 1] > curmax:
                curmax = nums[row][idx + 1]
            curmin = heap[0][0]

            # print("max min")
            # print(curmax)
            # print(curmin)
            if curmax - curmin < curminrange:
                retmax = curmax
                retmin = curmin
                curminrange = curmax - curmin

        return [retmin, retmax]