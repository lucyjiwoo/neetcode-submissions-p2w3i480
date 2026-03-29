class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def minDisRecur(s1,s2, m, n, memo):
            # Case 1: word1 is empty str
            if m == 0:
                return n
            # Case 2: word2 is empty str
            if n == 0:
                return m
            # if the memo is existed
            if memo[m][n] != -1:
                return memo[m][n]

            # if the last character is same
            if s1[m - 1] == s2[n - 1]:
                memo[m][n] = minDisRecur(s1, s2, m - 1, n - 1, memo)
                return memo[m][n]
            # The last char is not same -> Compare top-left vs top vs left
            memo[m][n] = 1 + min(minDisRecur(s1, s2, m, n - 1, memo), 
                                minDisRecur(s1, s2, m - 1, n, memo), 
                                minDisRecur(s1, s2, m - 1, n - 1, memo))
            return memo[m][n]

        m, n = len(word1), len(word2)
        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return minDisRecur(word1, word2, m, n, memo)
