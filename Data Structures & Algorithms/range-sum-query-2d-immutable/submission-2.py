class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.arr = matrix
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        l = col2 - col1 + 1
        b = row2 - row1 + 1
        total = 0
        for i in range(row1, row1 + b):
            for j in range(col1, col1 + l):
                total += self.arr[i][j]
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)