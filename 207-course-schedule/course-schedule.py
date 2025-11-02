class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(set)
        for pre, req in prerequisites:
            prereqs[pre].add(req)

        visited = set()

        def dfs(i):
            # print("dfs", i)
            if len(prereqs[i]) == 0:
                return True
            # else:
            #     print("i",i,"has prereqs", prereqs[i])

            if i in visited:
                # print("i", i, "in visited")
                return False

            visited.add(i)
            for req in prereqs[i]:
                if not dfs(req):
                    # print("dfs", i, "failed at", req)
                    return False
            visited.remove(i)

            prereqs[i] = set()
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True