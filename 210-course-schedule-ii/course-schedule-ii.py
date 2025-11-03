from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(set)
        for pre, req in prerequisites:
            prereqs[pre].add(req)

        visited = set()
        ret = []

        def dfs(i):
            # print("dfs", i)
            if len(prereqs[i]) == 0:
                if i not in ret:
                    ret.append(i)
                return True
            # else:
            #     print("i",i,"has prereqs", prereqs[i])

            if i in visited:
                # print("i", i, "in visited")
                return []

            visited.add(i)
            for req in prereqs[i]:
                if not dfs(req):
                    # print("dfs", i, "failed at", req)
                    return ret
            visited.remove(i)

            prereqs[i] = set()
            ret.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return ret