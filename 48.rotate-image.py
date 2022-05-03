#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
import numpy as np

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)

        matrix = np.transpose(matrix)

        # for i in range(l):
        #     for j in range(l):
        #         temp = matrix[i][j] 
        #         matrix[i][j] = matrix[j][i]
        #         matrix[j][i] = temp
        
        # for row in range(l):
        #     for pos in range(int(l/2)):
        #         temp = matrix[row][pos]
        #         matrix[row][pos] = matrix[row][l - 1 - pos]
        #         matrix[row][l - 1 - pos] = temp
    


        
# @lc code=end

