class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        Row = len(matrix)
        Col = len(matrix[0])
        res = []
        cycle = 0
        
        while len(res) < Row * Col:
            # right
            for i in range(cycle, Col - cycle):
                res.append(matrix[cycle][i])

            if len(res) >= Row * Col:
                break
            # down
            for i in range(1+cycle, Row - cycle - 1):
                res.append(matrix[i][Col - 1 -cycle])

            if len(res) >= Row * Col:
                break

            # left
            for i in range(Col - cycle - 1, cycle - 1, -1):
                res.append(matrix[Row - 1 - cycle][i])

            if len(res) >= Row * Col:
                break
            
            # up
            for i in range(Row - cycle - 2, cycle, -1):
                res.append(matrix[i][cycle])
            
            cycle += 1

        return res