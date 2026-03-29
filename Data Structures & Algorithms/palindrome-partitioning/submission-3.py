class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                res.append(path)
                return
            
            for end in range(start, len(s)):
                sub = s[start:end+1]
                if isPalindrome(sub):
                    backtrack(end+1, path + [sub])

        backtrack(0, [])
        return res