class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = dict()
        for num in nums:
            if num in mp:
                return True
            else:
                mp[num] = 1
        return False