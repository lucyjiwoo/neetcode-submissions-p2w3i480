class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list first
        sorted_nums = sorted(nums)
        res = []
        # iterate the index until it reachs last third index
        for i in range(len(sorted_nums)-2):

            if sorted_nums[i] > 0:
                break
            j = i+1     # start from ith next element
            k = len(sorted_nums)-1     # start from the last element
            while j < k:
                if sorted_nums[i] + sorted_nums[j]+ sorted_nums[k] == 0:
                    if [sorted_nums[i],sorted_nums[j],sorted_nums[k]] in res:
                        j += 1
                    else:
                        res.append([sorted_nums[i],sorted_nums[j],sorted_nums[k]])
                        j += 1
                elif sorted_nums[j]+ sorted_nums[k] < - sorted_nums[i]:
                    j += 1
                else:
                    k -= 1
        return res