class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initialize the two pointers
        # l for the start and r for the end
        l = 0
        r = len(s) - 1

        while l < r:
            # move l forward until it points to a letter
            while l < r and not self.alphaNum(s[l]):
                l += 1
            
            # move r backwards until it points to a letter
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            
            # compare the lowercase characters at l and r
            # return false if they dont match
            if s[l].lower() != s[r].lower():
                return False
            
            # move both points inward
            l += 1
            r -= 1
        
        return True
    
    # function for checking if its a letter or number
    def alphaNum(self, c):
        # ord() checks for the unicode of the character
        # so we're checking if the unicode is between the characters
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
