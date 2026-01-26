class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i in range(len(ranges)):
            intervals.append((i - ranges[i], i + ranges[i]))

        intervals.sort()
        print(intervals)

        c = 0
        cur_reach = -1
        while c < len(intervals) and intervals[c][0] <= 0:
            cur_reach = max(cur_reach, intervals[c][1])
            c += 1

        if cur_reach == -1:
            return -1
        if cur_reach >= n:
            return 1

        opened = 0
        max_reach = 0

        while c < len(intervals):
            if intervals[c][0] > cur_reach:
                return -1
            
            if intervals[c][0] > max_reach:
                print("cur reach max reach", cur_reach, max_reach)
                max_reach = cur_reach
                opened += 1
            
            cur_reach = max(cur_reach, intervals[c][1])
            c += 1
            if max_reach >= n:
                return opened

            if cur_reach >= n:
                return opened + 1

        return -1

            