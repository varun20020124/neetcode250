class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        top = 0
        bottom = m - 1
        while top<=bottom:
            mid = (top+bottom)//2
            if matrix[mid][-1] < target:
                top = mid+1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                break
        if not (top<=bottom):
            return False
        row = matrix[mid]
        l = 0
        h = n-1
        while l<=h:
            m = (l+h)//2
            if row[m] == target:
                return True
            elif row[m] > target:
                h = m-1
            else:
                l = m+1
        return False