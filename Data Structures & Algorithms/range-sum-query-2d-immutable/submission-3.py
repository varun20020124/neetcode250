class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m,n = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (n+1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.prefix_sum[i][j+1] = self.prefix_sum[i][j] + matrix[i][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for r in range(row1, row2+1):
            result += self.prefix_sum[r][col2+1] - self.prefix_sum[r][col1]
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)