class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lefts = [1] * len(nums)
        rights = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                lefts[i] = lefts[i-1] * nums[i-1]
        for j in reversed(range(len(nums))):
            if j == len(nums) - 1:
                continue
            else:
                rights[j] = rights[j+1] * nums[j+1]
        res = []
        for left, right in zip(lefts, rights):
            res.append(left*right)
        return res
            