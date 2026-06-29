class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # put all unique characters into a set
        # sets removes duplicates
        charSet = set(s)
        res = 0

        for c in charSet:
            # set count and l to 0
            count = l = 0

            # slide through with r
            for r in range(len(s)):
                # increase count
                if s[r] == c:
                    count += 1
                
                # if the window needs more than k
                # move l forward and adjust count
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                
                # update the result
                res = max(res, r - l + 1)
        
        return res

            
                

