class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row, column, sub-boxes
        ROWS, COLS = len(board), len(board)
        boxes = [set() for i in range((ROWS//3) * (COLS//3))]
        cols = [set() for i in range (COLS)]
        for r in range(ROWS):
            row = set()
            for c in range(COLS):
                if board[r][c] != ".":
                    if board[r][c] in row:
                        return False
                    else:
                        row.add(board[r][c])
                    if board[r][c] in cols[c]:
                        return False
                    else:
                        cols[c].add(board[r][c])
                    if board[r][c] in boxes[3*(r//3) + (c//3)]:
                        return False
                    else:
                        boxes[3*(r//3) + (c//3)].add(board[r][c])
        return True