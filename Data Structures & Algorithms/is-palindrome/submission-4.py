class Solution:
    def isPalindrome(self, s: str) -> bool:
        # join string without special characters
        # looping through each character and checking if they're a letter or number
        s1 = "".join([char for char in s if char.isalnum()])
        
        return s1.lower() == s1[::-1].lower()