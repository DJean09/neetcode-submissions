class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we want to know the position of the number in the list
        # so a dictionary works best
        numHash = {}
        num_len = len(nums)
        
        # this would check to see what number is needed to get the sum
        complement = 0
        
        for i in range(num_len):
            complement = target - nums[i]
            if complement in numHash:
                return [numHash[complement], i]
            numHash[nums[i]] = i
        
        # if nothing is found
        return []