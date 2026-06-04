class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = 0
        num_len = len(nums)
        numHash = {} # We want the position in the list so we're using a Hash

        for i in range(num_len):
            compliment = target - nums[i]
            if compliment in numHash:
                return [numHash[compliment], i]
            numHash[nums[i]] = i