from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(set)
        res = []
        seen = set()
        leadsto = defaultdict(set)

        for pre, req in prerequisites:
            prereqs[pre].add(req)
            leadsto[req].add(pre)

        cantake = deque()
        for i in range(numCourses):
            if len(prereqs[i]) == 0:
                cantake.append(i)

        while cantake:
            course = cantake.popleft()
            seen.add(course)
            res.append(course)
            for next_course in leadsto[course]:
                prereqs[next_course].remove(course)
                if len(prereqs[next_course]) == 0:
                    if next_course not in seen:
                        cantake.append(next_course)

        if len(res) == numCourses:
            return res
        return []