class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if length is the same
        if len(s) != len(t):
            return False
        
        # Use the sorted() function to compare
        return sorted(s) == sorted(t)