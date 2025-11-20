import copy


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        R = len(board)
        C = len(board[0])
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        dir = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        def bomb_nei(r,c):
            count = 0

            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if board[nr][nc] == 'M':
                        count += 1

            return count

        def reveal_recursive(r, c):
            q = deque()
            q.append((r, c))
            seen = set()

            while q:
                pr, pc = q.popleft()
                num_nei = bomb_nei(pr, pc)
                if num_nei == 0:
                    # print(pr, pc, "zero bombs")
                    board[pr][pc] = 'B'
                    for dr, dc in dir:
                        nr, nc = pr + dr, pc + dc
                        if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in seen:
                            seen.add((nr, nc))
                            q.append((nr, nc))
                else:
                    board[pr][pc] = str(num_nei)
                    
        r, c = click[0], click[1]
        if board[r][c] == "M":
            board[r][c] = 'X'
            return board
        elif board[r][c] == 'E':
            num_nei = bomb_nei(r, c)
            if num_nei == 0:
                reveal_recursive(r, c)
            else:
                board[r][c] = str(num_nei)

        # print(bomb_nei(0,0))
        # print(bomb_nei(2, 1))
        # print(bomb_nei(1, 2))
        # print(bomb_nei(1, 3))
        # print(bomb_nei(1, 4))
        
        return board
        