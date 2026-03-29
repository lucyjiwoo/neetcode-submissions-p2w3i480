class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # build hashmap for digits and corresponding letters
        mp = ["#", "#", "abc","def", "ghi","jkl","mno","pqrs","tuv","wxyz"]
        res = []
        def backtracking(i, word=""):
            if i == len(digits):
                if word:
                    res.append(word)
                return
            for ch in mp[int(digits[i])]:
                backtracking(i+1,word+ch)
        backtracking(0,"")
        return res