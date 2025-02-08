class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        if not matrix:
            return
        self.dp[0][0] = matrix[0][0]
        for i in range(1, len(matrix)):
            self.dp[i][0] = self.dp[i - 1][0] + matrix[i][0]

        for i in range(1, len(matrix[0])):
            self.dp[0][i] = self.dp[0][i - 1] + matrix[0][i]

        for r in range(1, len(matrix)):
            cur = matrix[r][0]
            for c in range(1, len(matrix[0])):
                cur += matrix[r][c]
                self.dp[r][c] = self.dp[r - 1][c] + cur

        for r in range(len(matrix)):
            print(self.dp[r])
                


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.dp[row2][col2]
        elif row1 == 0:
            return self.dp[row2][col2] - self.dp[row2][col1 - 1]
        elif col1 == 0:
            return self.dp[row2][col2] - self.dp[row1 - 1][col2]
        else:
            return self.dp[row2][col2] - self.dp[row2][col1-1] - self.dp[row1-1][col2] + self.dp[row1 - 1][col1 - 1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)