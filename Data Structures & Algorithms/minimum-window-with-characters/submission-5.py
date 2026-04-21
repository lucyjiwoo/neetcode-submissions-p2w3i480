class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge Case
        # if t is empty or s is smallar than than t
        if t == "" or len(t) > len(s):
            return ""

        countT, window = {}, {}
        have, need = 0, len(t)
        res, resLen = [0,0], float("infinity")
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in countT and countT[s[r]] >= window[s[r]]:
                have += 1
            
            while need == have:
                if (r-l+1) < resLen:
                    resLen = r-l +1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
                
        return "" if resLen == float("infinity") else s[res[0]:res[1]+1]