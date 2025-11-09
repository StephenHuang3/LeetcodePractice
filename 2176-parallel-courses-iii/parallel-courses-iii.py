from collections import defaultdict, deque
import heapq


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        leadsto = defaultdict(list)
        prereqs = defaultdict(set)

        for prev, nxt in relations:
            leadsto[prev].append(nxt)
            prereqs[nxt].add(prev)

        hp = []
        cur_time = 0
        for i in range(1, n + 1, 1):
            if not prereqs[i]:
                heapq.heappush(hp, (time[i - 1] + cur_time, i))
        # print(hp)
        while hp:
            finish_time, finished_course = heapq.heappop(hp)
            cur_time = finish_time
            for nxt in leadsto[finished_course]:
                prereqs[nxt].discard(finished_course)
                if len(prereqs[nxt]) == 0:
                    heapq.heappush(hp, (cur_time + time[nxt - 1], nxt))

        return cur_time