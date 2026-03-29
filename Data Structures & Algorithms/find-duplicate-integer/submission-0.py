class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        compare = [1] * (len(nums)-1)
        for num in nums:
            if compare[num - 1] == 0:
                return num
            else:
                compare[num - 1] -= 1
