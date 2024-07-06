class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def surrounded(r, c, visited):
            if (r, c) in visited or r < 0 or c < 0 or r == len(board) or c == len(board[0]):
                return True
            visited.add((r, c))
            if board[r][c] == "X":
                return True
            elif board[r][c] == "O" and (r == 0 or c == 0 or r == len(board) - 1 or c == len(board[0]) - 1):
                return False
            else:
                return surrounded(r - 1, c, visited) and surrounded(r + 1, c, visited) and surrounded(r, c - 1, visited) and surrounded(r, c + 1, visited)

        def fill(r, c, filled):
            if (r, c) in filled or r < 0 or c < 0 or r == len(board) or c == len(board[0]):
                return
            filled.add((r, c))
            if board[r][c] == "X":
                return
            board[r][c] = "X"
            fill(r + 1, c, filled)
            fill(r - 1, c, filled)
            fill(r, c - 1, filled)
            fill(r, c + 1, filled)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    visited = set()
                    if surrounded(r, c, visited):
                        filled = set()
                        fill(r, c, filled)

                

        """
        Do not return anything, modify board in-place instead.
        """
        