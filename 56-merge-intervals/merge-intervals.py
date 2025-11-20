class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = [intervals[0]]
        
        for interval in intervals:
            if ret[-1][-1] >= interval[0]:
                ret[-1][-1] = max(interval[-1], ret[-1][-1])
            else:
                ret.append(interval)

        return ret