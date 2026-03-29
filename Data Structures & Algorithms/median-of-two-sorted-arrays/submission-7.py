class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = (len(nums1)+ len(nums2))//2 +1
        l, r = 0, 0
        sorted_list = []
        while l + r < m:
            if l < len(nums1) and r <len(nums2):
                if nums1[l] <= nums2[r]:
                    sorted_list.append(nums1[l])
                    l += 1
                else:
                    sorted_list.append(nums2[r])
                    r += 1
            elif r < len(nums2):
                sorted_list.append(nums2[r])
                r += 1
            else:
                sorted_list.append(nums1[l])
                l += 1
        if (len(nums1) + len(nums2)) % 2 == 1:
            return float(sorted_list[-1])
        else:
            last = sorted_list.pop()
            second = sorted_list.pop()
            return (last + second)/2
