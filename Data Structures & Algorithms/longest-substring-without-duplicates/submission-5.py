class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Find the substring any char is duplicated
        # Find the longest substring

        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res