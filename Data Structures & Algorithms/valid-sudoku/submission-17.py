class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows,cols,boxes = set(), set(), set()
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue
                num = board[r][c]
                box = (r//3,c//3)
                if (r,num) in rows: return False
                if (c,num) in cols: return False
                if (box,num) in boxes: return False
                rows.add((r,num))
                cols.add((c,num))
                boxes.add((box,num))
        return True