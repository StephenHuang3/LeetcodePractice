#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        posr = 0
        row = len(matrix)
        column = len(matrix[0])

        while len(ans) < row * column:
            for x in range(column - 2 * posr):
                ans.append(matrix[posr][x + posr])

            if len(ans) >= row * column:
                break
            
            for y in range(row - 2 - 2 * posr):
                ans.append(matrix[y + posr + 1][column - 1 -posr]);
            
            if len(ans) >= row * column:
                break

            for x in range(column - 2 * posr):
                ans.append(matrix[row - posr - 1][column - x - 1 - posr])

            if len(ans) == row * column:
                break

            for y in range(row - 2 - 2 * posr):
                ans.append(matrix[row - y - 2 - posr][posr])
            
            posr += 1

        return ans

        
# @lc code=end

