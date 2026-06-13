class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = []
        nums_set = set(nums)
        res = 0
        while nums_set:
            if not seq:
                n = nums_set.pop()
                seq = [n,n]
            elif seq[0] - 1 in nums_set or seq[1] + 1 in nums_set:
                if seq[0] - 1 in nums_set:
                    nums_set.remove(seq[0] - 1)
                    seq[0] = seq[0] - 1
                else:
                    nums_set.remove(seq[1] + 1)
                    seq[1] = seq[1] + 1
            else:
                res = max(res, seq[1] - seq[0] + 1)
                seq = []
        return max(res, seq[1] - seq[0] + 1) if seq else res


