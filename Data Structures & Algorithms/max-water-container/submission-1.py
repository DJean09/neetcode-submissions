class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # set result and l/r pointers
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            # find the current area
            area = min(heights[l], heights[r]) * (r - l)

            # update result
            res = max(area, res)

            # move the pointer at the shorter height
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return res