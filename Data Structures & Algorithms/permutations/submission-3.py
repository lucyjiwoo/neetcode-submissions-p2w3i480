class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        mp = {n: 1 for n in nums}

        def backtracking(mp, perm):
            if not mp:
                res.append(perm[:])   # 복사
                return

            for num in mp:
                c = dict(mp)
                c.pop(num)

                perm.append(num)
                backtracking(c, perm)
                perm.pop()   

        backtracking(mp, [])
        return res
