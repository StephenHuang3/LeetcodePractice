from collections import defaultdict, deque
import heapq


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        prereqs = defaultdict(list)
        max_time = {}
        
        for prev, nxt in relations:
            prereqs[nxt].append(prev)

        
        def dfs(course):
            if course in max_time:
                return max_time[course]
            
            course_time = time[course - 1]
            dependents_time = 0

            for req in prereqs[course]:
                dependents_time = max(dependents_time, dfs(req))

            max_time[course] = course_time + dependents_time

            return course_time + dependents_time

        for i in range(1, n + 1, 1):
            dfs(i)
        return max(max_time.values())

            