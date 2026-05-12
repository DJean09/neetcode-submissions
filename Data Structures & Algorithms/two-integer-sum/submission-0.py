class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        numHash = {}
        compliment = 0
        
        for i in range(len_nums):
            compliment = target - nums[i]
            if compliment in numHash:
                return [numHash[compliment], i]
            numHash[nums[i]] = i

        return []