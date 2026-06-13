class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = dict()
        for i in range(len(numbers)):
            if target - numbers[i] in mp and numbers[i] != target - numbers[i]:
                return [mp[target - numbers[i]], i + 1]
            mp[numbers[i]] = i + 1
        
