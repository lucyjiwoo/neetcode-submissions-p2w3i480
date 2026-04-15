class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = dict()
        for s in strs:
            alp = [0]*26
            for ch in s:
                alp[ord(ch)- ord("a")] += 1
            if tuple(alp) in mp:
                mp[tuple(alp)].append(s)
            else:
                mp[tuple(alp)] = [s]
        res = []
        for w in mp.values():
            res.append(w)
        return res