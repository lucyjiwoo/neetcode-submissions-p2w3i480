class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Placing N queens in n x n board
        # return all possible solutions

        # one queen in each row, col
        # no diagonal

        # set queen in ith row append()
        # find possible queen positions in next row. 
        # if no possible positions, then skip (backtrack)
        # if it reach last row, then append solution to result.

        # Update possible positions.
        # pop col, row
        # How to find diagonal?

        res = []
        if not n:
            return [[]]
        def is_Valid(row,col, pos = []):
            for p in pos:
                if p[0]== row or p[1]== col:
                    return False
                if abs(p[0] - row) == abs(p[1]-col):
                    return False
            return True
        def backtrack(row, pos = [], sol=[]):
            if len(sol) == n:
                
                res.append(sol)
                return
            for col in range(n):
                if is_Valid(row, col, pos):
                    s = ["."] * n
                    s[col] = "Q"
                    backtrack(row+1, pos[:]+[[row,col]], sol[:] + ["".join(s)])
        backtrack(0,[],[])
        return res
