class Solution:
    def isPalindrome(self, s: str) -> bool:
        # palindrome[backward == forward], ignore non alphanumeric chars

        # Two pointers, left and right
        # iterate until left >= right
        # in the loop Condition: if alphanumeric => check if left == right\
        # no alphanumeric ==> move pointers
        if len(s) <=1:
            return True
        l,r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
                

            
            
