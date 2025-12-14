import heapq


class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        num_len = len(nums[0])
        ret = []
        trim2arr = {}

        for k, trim in queries:
            if trim in trim2arr:
                continue
            else:
                trimmed = [(int(num[num_len - trim:]), i) for i, num in enumerate(nums)]
                trimmed.sort()
                trim2arr[trim] = trimmed

        for k, trim in queries:
            trimmed = trim2arr[trim]
            ret.append(trimmed[k - 1][1])

        return ret