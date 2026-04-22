class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            if nums[abs(num)] < 0:
                nums[abs(num)] = abs(nums[abs(num)])
                return abs(num)
            nums[abs(num)] = -abs(nums[abs(num)])
        return -1
