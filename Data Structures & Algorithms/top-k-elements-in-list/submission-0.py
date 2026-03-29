class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        rev_freq = dict()
        for num, freq in freq.items():
            if freq in rev_freq:
                rev_freq[freq].append(num)
            else:
                rev_freq[freq] = [num]
        count = 0
        result = []
        i = len(nums)
        while count < k and i > 0:
            if i in rev_freq:
                result += rev_freq[i]
                count += len(rev_freq[i])
            i -= 1
        return result
