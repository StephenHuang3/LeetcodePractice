class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        res = []
        count = 0
        vert_taken = set()
        horz_taken = set()
        pos_diag_taken = set()
        neg_diag_taken = set()

        def allowed(r, c) -> bool:
            # print("cur state input", r, c)
            # print(horz_taken)
            # print(vert_taken)
            # print(pos_diag_taken)
            # print(neg_diag_taken)
            if r in horz_taken or c in vert_taken:
                # print("fail due to horz, vert")
                return False

            pos_diag = c - r
            neg_diag = c + r
            if pos_diag in pos_diag_taken or neg_diag in neg_diag_taken:
                # print("fail due to diag")
                return False

            horz_taken.add(r)
            vert_taken.add(c)
            pos_diag_taken.add(pos_diag)
            neg_diag_taken.add(neg_diag)

            return True

        def remove(r, c) -> None:
            horz_taken.remove(r)
            vert_taken.remove(c)
            pos_diag_taken.remove(c - r)
            neg_diag_taken.remove(c + r)



        def backtrack(r, c) -> None:
            # base case
            nonlocal count
            if count == n:
                print(board)
                res.append(["".join(board[i].copy()) for i in range(n)])
                return
            if r == n:
                return

            newc = (c + 1) % n
            newr = r if c != n -1 else r + 1
            
            # try queen:
            board[r][c] = "Q"
            if allowed(r, c):
                count += 1
                backtrack(newr, newc)
                remove(r, c)
                count -= 1
            
            # regular
            board[r][c] = "."
            backtrack(newr, newc)

        backtrack(0,0)

        return res
