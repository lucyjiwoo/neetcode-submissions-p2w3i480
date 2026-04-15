class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Two pointers and visited list 
        # 1. sort the list, if num1 is positive, then no need to iterate 
        res = []
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            if nums[i] > 0:
                break
            while j < len(nums)-1 and nums[j] <= -nums[i] :
                if -nums[i]-nums[j] in nums[j+1:]:
                    if [nums[i],nums[j], -nums[i]-nums[j]] not in res:
                        res.append([nums[i],nums[j], -nums[i]-nums[j]])
                j += 1
        return res