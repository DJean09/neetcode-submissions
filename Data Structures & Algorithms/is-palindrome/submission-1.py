class Solution:
    def isPalindrome(self, s: str) -> bool:
        # blank string
        cleaned = ""
        # iterate through each letter in the string
        for char in s:
            # isalnum() checks if its a letter/number with no special characters
            if char.isalnum():
                # make sure its lowercase
                cleaned += char.lower()
        # return the comparison results
        return cleaned == cleaned[::-1]