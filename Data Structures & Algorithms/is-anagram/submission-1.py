class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        if s == t:
            return True

        ch_s, ch_t = [0]*26, [0]*26

        for i in range(len(s)):
            ch_s[ord(s[i])- ord("a")] += 1
            ch_t[ord(t[i])- ord("a")] += 1
        
        return ch_s == ch_t