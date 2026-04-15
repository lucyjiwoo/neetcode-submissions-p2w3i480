class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r = [1]*len(nums), [1]*len(nums)
        for i in range(len(nums)):
            if i > 0:
                l[i] = l[i-1] * nums[i-1]
            j = len(nums)-i-1
            if j < len(nums) - 1:
                r[j] = r[j+1] * nums[j+1]
        res = []
        for n in range(len(nums)):
            res.append(l[n]*r[n])
        return res