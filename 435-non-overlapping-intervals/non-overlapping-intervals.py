class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals.sort(key=lambda x: x[1])
        last_finish = intervals[0][1]
        removed = 0

        for begin, end in intervals[1:]:
            if begin < last_finish:
                removed += 1
                continue
            last_finish = end

        return removed