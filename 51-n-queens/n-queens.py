class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        count = 0
        res = []
        vert_taken = set()
        pos_diag_taken = set()
        neg_diag_taken = set()

        def backtrack(r) -> None:
            nonlocal count
            if r == n:
                res.append(["".join(board[i]) for i in range(n)])
                return

            for c in range(n):
                if c not in vert_taken and (r - c) not in pos_diag_taken and (r + c) not in neg_diag_taken:
                    board[r][c] = "Q"
                    count += 1
                    vert_taken.add(c); pos_diag_taken.add(r- c); neg_diag_taken.add(r + c)
                    backtrack(r + 1)
                    vert_taken.remove(c); pos_diag_taken.remove(r - c); neg_diag_taken.remove(r + c)
                    board[r][c] = "."
            

        backtrack(0)

        return res
