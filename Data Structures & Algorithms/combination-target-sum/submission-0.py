class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, i = [], 0
        nums = list(set(nums))
        nums.sort()
        def backtracking(i, target, comb = []):
            if i == len(nums):
                return
            if nums[i] > target:
                return
            elif nums[i] == target:
                comb.append(nums[i])
                res.append(comb)
                return
            else:
                # Include nums[i]
                backtracking(i, target - nums[i], comb + [nums[i]])
                # Not include nums[i]
                backtracking(i+1, target, comb)
        backtracking(i, target, [])
        return res