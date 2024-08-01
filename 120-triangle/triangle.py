class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in range(1, len(triangle)):
            for i in range(len(triangle[r])):
                if i == 0:
                    triangle[r][i] += triangle[r - 1][i]
                elif i == len(triangle[r]) - 1:
                    triangle[r][i] += triangle[r - 1][i - 1]                    
                else:
                    triangle[r][i] += min(triangle[r - 1][i], triangle[r - 1][i - 1])

        # print(triangle[len(triangle) - 1])
        return min(triangle[len(triangle) - 1])