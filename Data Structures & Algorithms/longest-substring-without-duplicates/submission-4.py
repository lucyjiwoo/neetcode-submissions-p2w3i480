class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_sub = ""
        i, res = 0, 0

        while i < len(s):
            if s[i] in current_sub:
                current_sub = current_sub[1:]
            else:
                current_sub += s[i]
                res = max(res, len(current_sub))
                i +=1
        return res

        

