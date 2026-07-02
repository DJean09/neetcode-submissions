class Solution:
    def trap(self, height: List[int]) -> int:
        # return 0 if emtpy
        if not height:
            return 0

        # set pointers
        l, r = 0, len(height) - 1
        # track tallest walls
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                # if the left tallest is smaller
                # move l to the right and update left tallest
                l += 1
                leftMax = max(leftMax, height[l])
                
                # add leftmax - height to result
                res += leftMax - height[l]
            else:
                # same thing but for r going left
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res