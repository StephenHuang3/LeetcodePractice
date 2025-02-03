class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)
        visited = set()

        for pre, req in prerequisites:
            prereq[pre].append(req)
        
        cantake = 0

        def dfs(course):
            if len(prereq[course]) == 0:
                return True
            if course in visited:
                return False
            
            for cur in prereq[course]:
                visited.add(course)
                if not dfs(cur):
                    visited.remove(course)
                    return False

                visited.remove(course)

            prereq[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

