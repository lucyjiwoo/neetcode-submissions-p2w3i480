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
            if not s[l].isalnum() or not s[r].isalnum():
                if not s[l].isalnum():
                    l += 1
                if not s[r].isalnum():
                    r -= 1
                continue
            else:
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
            
        return True

            
            
