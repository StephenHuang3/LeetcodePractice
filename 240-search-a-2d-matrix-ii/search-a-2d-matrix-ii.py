class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])

        pr = 0
        pc = C - 1
        
        while pr < R and pc >= 0:
            if matrix[pr][pc] == target:
                return True
            elif target < matrix[pr][pc]:
                pc -= 1
            else:
                pr += 1

        return False