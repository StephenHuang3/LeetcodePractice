import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda i: i[1])
        total_days = 0
        hp = []

        for i in range(len(courses)):

            total_days += courses[i][0]
            heapq.heappush(hp, -courses[i][0])
            if total_days > courses[i][1]:
                total_days += heapq.heappop(hp)
        
        return len(hp)