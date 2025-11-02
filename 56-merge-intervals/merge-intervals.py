class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = []
        for start, end in intervals:
            if ret and start <= ret[-1][1]:
                ret[-1][1] = max(end, ret[-1][1])
            else:
                ret.append([start, end])

        return ret