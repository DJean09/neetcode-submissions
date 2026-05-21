class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = 0
        num_len = len(nums)
        numHash = {}

        for i in range(num_len):
            complement = target - nums[i]
            if complement in numHash:
                return [numHash[complement], i]
            numHash[nums[i]] = i
        
        return []