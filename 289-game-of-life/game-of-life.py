class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        # def findLive(m, n, r, c):
        #     tot = 0
        #     if c - 1 >= 0:
        #         tot += board[r][c - 1]
        #         if r - 1 >= 0:
        #             tot += board[r - 1][c - 1]
        #         if r + 1 < m:
        #             tot += board[r + 1][c - 1]

        #     if r - 1 >= 0:
        #         tot += board[r - 1][c]
        #     if r + 1 < m:
        #         tot += board[r + 1][c]

        #     if c + 1 < n:
        #         tot += board[r][c + 1]
        #         if r - 1 >= 0:
        #             tot += board[r - 1][c + 1]
        #         if r + 1 < m:
        #             tot += board[r + 1][c + 1]

        #     return tot

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] % 10 == 1:
                    if c - 1 >= 0:
                        board[r][c - 1] += 10
                        if r - 1 >= 0:
                            board[r - 1][c - 1] += 10
                        if r + 1 < m:
                            board[r + 1][c - 1] += 10

                    if r + 1 < m:
                        board[r + 1][c] += 10
                    if r - 1 >= 0:
                        board[r - 1][c] += 10

                    if c + 1 < n:
                        board[r][c + 1] += 10
                        if r - 1 >= 0:
                            board[r - 1][c + 1] += 10
                        if r + 1 < m:
                            board[r + 1][c + 1] += 10
        
        for r in range(m):
            for c in range(n):
                if board[r][c] % 10 == 1:
                    if (board[r][c] // 10) < 2:
                        board[r][c] = 0
                    elif (board[r][c] // 10) > 3:
                        board[r][c] = 0
                    else:
                        board[r][c] = 1
                else:
                    if board[r][c] // 10 == 3:
                        board[r][c] = 1
                    else:
                        board[r][c] = 0