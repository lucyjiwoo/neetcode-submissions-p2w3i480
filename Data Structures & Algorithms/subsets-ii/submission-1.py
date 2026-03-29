class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtracking(i, subset):
            if i == len(nums):
                if subset not in res:
                    res.append(subset)
                return
            backtracking(i + 1, subset + [nums[i]])
            backtracking(i + 1, subset)
        backtracking(0, [])
        return res