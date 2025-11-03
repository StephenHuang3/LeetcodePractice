from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        leads_to = defaultdict(list)
        indegree = [0] * numCourses
        for pre, req in prerequisites:
            leads_to[req].append(pre)
            indegree[pre] += 1

        q = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
        ret = [x for x in q]

        while q:
            node = q.popleft()

            for next_course in leads_to[node]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)
                    ret.append(next_course)
            leads_to[node] = []

        return ret if len(ret) == numCourses else []

        