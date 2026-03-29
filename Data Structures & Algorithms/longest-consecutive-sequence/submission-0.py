class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def findConsecutive(current, nums, visited, seq):
            if current + 1 in nums and current + 1 not in visited:
                seq.add(current + 1)
                visited.append(current + 1)
                findConsecutive(current +1, nums, visited, seq)
            if current - 1 in nums and current - 1 not in visited:
                seq.add(current - 1)
                visited.append(current - 1)
                findConsecutive(current - 1, nums, visited, seq)
            return seq
        
        visited = []
        res  = 0
        i = 0
        while i < len(nums):
            if nums[i] in visited:
                i += 1
                continue
            visited.append(nums[i])
            res = max( res, len(findConsecutive(nums[i],nums,visited,set([nums[i]]))))
        return res