class Solution:
    def isPalindrome(self, s: str) -> bool:
        # much faster, 2 pointers method
        # set pointers
        front = 0
        back = len(s) - 1

        # keep iterating until they meet halfway
        while front < back:
            # skip special characters
            while front < back and not s[front].isalnum():
                front += 1
            while back > front and not s[back].isalnum():
                back -= 1
            # check if each character matches
            if s[front].lower() != s[back].lower():
                return False
            # increment up
            front += 1
            back -= 1
        
        return True