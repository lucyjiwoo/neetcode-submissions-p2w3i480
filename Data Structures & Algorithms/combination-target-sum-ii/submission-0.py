class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        i, res = 0, []
        def backtracking(i, target, comb):
            if i == len(candidates):
                return 
            if candidates[i] > target:
                return
            elif candidates[i] == target:
                comb.append(candidates[i])
                if comb not in res:
                    res.append(comb)
                return
            backtracking(i+1, target - candidates[i], comb + [candidates[i]])
            backtracking(i +1, target, comb)
        backtracking(i, target, [])
        return res