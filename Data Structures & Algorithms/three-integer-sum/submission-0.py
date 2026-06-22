class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array to handle duplicates and allow two pointer
        res = []
        nums.sort()

        # loop through enumerated list
        for i, a in enumerate(nums):
            # break if all remaining numbers are positive
            if a > 0:
                break
            
            # skip duplicate values for the first number
            if i > 0 and a == nums[i - 1]:
                continue
            
            # set pointers
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                if threeSum > 0:
                    # if the sum is greater than 0, move r left
                    r -= 1
                elif threeSum < 0:
                    # if less, move l right
                    l += 1
                else:
                    # add to result
                    res.append([a, nums[l], nums[r]])

                    # move both points inwards and skip duplicates at the left pointer
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res