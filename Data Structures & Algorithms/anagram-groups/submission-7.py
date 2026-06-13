class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = dict()

        for s in strs:
            count = ["0"] * 26
            for c in s:
                count[ord(c)- ord('a')] = str(int(count[ord(c)- ord('a')]) + 1)
            
            count_str = " ".join(count)
            if count_str in mp:
                mp[count_str].append(s)

            else:
                mp[count_str] = [s]
        return list(mp.values())