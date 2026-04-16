class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1, index2 = 1, len(numbers)
        while index1 < index2:
            if numbers[index1-1] + numbers[index2-1] < target:
                index1 +=1
            elif numbers[index1-1] + numbers[index2-1] > target:
                index2 -=1
            else:
                return [index1, index2]