class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            # A-Z, a-z, 0-9
            if s[left].isalnum():
                if s[right].isalnum():
                    if s[left].lower() != s[right].lower():
                        return False
                    else:
                        left += 1
                        right -= 1
                else:
                    right -= 1
            elif s[right].isalnum():
                left += 1
            else:
                left += 1
                right -= 1
        return True

            
            
