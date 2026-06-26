class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # empty set variable with 2 pointers
        seen = set()
        # l is left edge of the window
        l = 0
        res = 0

        # r is right edge that moves through the string
        for r in range(len(s)):
            while s[r] in seen:
                # removes s[l] from the set and move l right
                seen.remove(s[l])
                l += 1
            # add s[r] to the set
            seen.add(s[r])
            res = max(res, r - l + 1)
        
        return res

