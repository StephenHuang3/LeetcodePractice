#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rep = [0,0,0,0,0,0,0,0,0,0]

        for row in board:
            for number in row:
                if(number == "."):
                    continue
                if(int(number) >= 1 and int(number) <= 9):
                    rep[int(number)] += 1
            
            for x in range(10):
                if rep[x] > 1:
                    return False
            
            for x in range(10):
                rep[x] = 0

        for column in range(9):
            for row in range(9):
                if(board[row][column] == "."):
                    continue
                if(int(board[row][column]) >=1 and int(board[row][column]) <= 9):
                    rep[int(board[row][column])] += 1
            
            for x in range(10):
                if rep[x] > 1:
                    return False

            for x in range(10):
                rep[x] = 0

        for posx in range(0, 7, 3):
            for posy in range(0, 7, 3):

                for column in range(3):
                    for row in range(3):
                        if(board[column + posx][row + posy] == '.'):
                            continue
                        rep[int(board[column + posx][row + posy])] += 1
                
                for x in range(10):
                        if rep[x] > 1:
                            return False

                for x in range(10):
                    rep[x] = 0

        return True
        
# @lc code=end

