class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row and column check
        m,n = len(board), len(board[0])
        for i in range(m):
            hset = set()
            vset = set()
            for j in range(n):
                point = board[i][j]
                if board[i][j]!=".":
                    if board[i][j] not in hset:
                        hset.add(board[i][j])
                    else:
                        return False
                if board[j][i]!=".":
                    if board[j][i] not in vset:
                        vset.add(board[j][i])
                    else:
                        return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                box = set()
                for k in range(3):
                    for l in range(3):
                        square = board[i+k][j+l]
                        if square!=".":
                            if square not in box:
                                box.add(square)
                            else:
                                return False
        return True