class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def rec(i , subset = []):
            if i == len(nums):
                res.append(subset)
                return
            rec(i + 1, subset + [nums[i]])   
            rec(i + 1, subset)              
        rec(0, [])
        return res
            
