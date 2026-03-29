class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # build hashmap for digits and corresponding letters
        alpha = "abcdefghijklmno"
        res = []
        def backtracking(i , word=""):
            if i == len(digits):
                if word:
                    res.append(word)
                return
            if int(digits[i]) <=6:
                s = alpha[(int(digits[i])- 2)*3:(int(digits[i])- 1)*3]
            else:
                if int(digits[i]) == 7:
                    s = "pqrs"
                elif int(digits[i]) == 8:
                    s = "tuv"
                else:
                    s = "wxyz"
            for ch in s:
                backtracking(i+1,word+ch)
        backtracking(0,"")
        return res