class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We need position and value of array, so hash
        numHash = {}
        num_len = len(nums)
        complement = 0

        # iterate through
        for i in range(num_len):
            # check the complement
            complement = target - nums[i]
            # see if its in the hash already
            if complement in numHash:
                return [numHash[complement], i]
            # add to the hash
            numHash[nums[i]] = i
        
        # if nothing is found
        return []