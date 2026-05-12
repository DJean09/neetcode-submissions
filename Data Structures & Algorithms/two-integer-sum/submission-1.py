class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = 0
        num_len = len(nums)
        numHash = {}

        for i in range(num_len):
            # find the missing pair for sum
            complement = target - nums[i]
            # check if its in the hash map already
            if complement in numHash:
                return [numHash[complement], i]
            # add to the hashmap
            numHash[nums[i]] = i
        return []