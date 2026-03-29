class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Store index1, and index2
        index_1 = 1
        index_2 = len(numbers)
        while index_1 < index_2:
            if numbers[index_1 - 1] + numbers[index_2 - 1] == target:
                return [index_1, index_2]
            elif numbers[index_1-1] + numbers[index_2-1] < target:
                index_1 += 1
            else:
                index_2 -= 1
        
        