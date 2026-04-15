class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = dict()
        for n in range(len(nums)):
            if nums[n] in mp:
                return [mp[nums[n]], n]
            comp = target - nums[n]
            mp[comp] = n
        
        