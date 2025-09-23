from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row and col no repeat check
        rows = defaultdict(set)
        cols = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != "." and (board[r][c] in rows[r] or board[r][c] in cols[c]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])

        # quadrant check
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # print("i, j", i, j)
                quadrant = set()
                for r in range(i, i + 3, 1):
                    for c in range(j, j + 3, 1):
                        if board[r][c] != "." and board[r][c] in quadrant:
                            return False
                        quadrant.add(board[r][c])

        return True


# [".",".",".",".","5",".",".","1","."],
# [".","4",".","3",".",".",".",".","."],
# [".",".",".",".",".","3",".",".","1"],
# ["8",".",".",".",".",".",".","2","."],
# [".",".","2",".","7",".",".",".","."],
# [".","1","5",".",".",".",".",".","."],
# [".",".",".",".",".","2",".",".","."],
# [".","2",".","9",".",".",".",".","."],
# [".",".","4",".",".",".",".",".","."]

# ["5","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]]