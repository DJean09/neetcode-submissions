class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if they're not already the same length
        if len(s) != len(t):
            return False
        
        # return the sorted list of the string
        return sorted(s) == sorted(t)