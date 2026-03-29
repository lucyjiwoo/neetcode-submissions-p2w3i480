class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows,cols,blocks = dict(),dict(),dict()
        for row in range(9):
            for col in range(9):
                block = str(row//3 + 1)+"-"+ str(col//3 + 1)
                # Digit
                if board[row][col].isdigit():
                    if 1<= int(board[row][col]) <= 9:
                        # Row Check
                        if row in rows:
                            before  = len(rows[row])
                            rows[row].add(board[row][col])
                            after = len(rows[row])
                            if after == before:
                                return False
                        else:
                            rows[row] = set(board[row][col])
                        # Col Check
                        if col in cols:
                            before  = len(cols[col])
                            cols[col].add(board[row][col])
                            after = len(cols[col])
                            if after == before:
                                return False
                        else:
                            cols[col] = set(board[row][col])
                        # Row Check
                        if block in blocks:
                            before  = len(blocks[block])
                            blocks[block].add(board[row][col])
                            after = len(blocks[block])
                            if after == before:
                                return False
                        else:
                            blocks[block] = set(board[row][col])
                    # Validitiy Check(1-9)
                    else:
                        return False
                # "."
                else:
                    continue
        return True
                
                    