class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(l, r, s):
            if l == r == n:
                res.append(s)
                return 
            elif l == r:
                backtracking(l + 1, r, s + "(")
            elif l == n: 
                backtracking(l , r + 1, s + ")")
            else:
                backtracking(l + 1, r, s + "(")
                backtracking(l , r + 1, s + ")")
        backtracking(0,0,"")
        return res

