class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list first
        nums.sort()
        res = []
        # iterate the index until it reachs last third index
        for i in range(len(nums)-2):

            if nums[i] > 0:
                break
            j = i+1     # start from ith next element
            k = len(nums)-1     # start from the last element
            while j < k:
                if nums[i] + nums[j]+ nums[k] == 0:
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                elif nums[j]+ nums[k] < - nums[i]:
                    j += 1
                else:
                    k -= 1
        return res