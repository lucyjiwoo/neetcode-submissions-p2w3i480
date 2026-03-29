class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # build hashmap for digits and corresponding letters
        mp = {}
        mp["2"], mp["3"] = "abc","def"
        mp["4"], mp["5"], mp["6"] = "ghi","jkl","mno"
        mp["7"], mp["8"], mp["9"] = "pqrs","tuv","wxyz"
        res = []
        def backtracking(i, word=""):
            if i == len(digits):
                if word:
                    res.append(word)
                return
            for ch in mp[digits[i]]:
                backtracking(i+1,word+ch)
        backtracking(0,"")
        return res