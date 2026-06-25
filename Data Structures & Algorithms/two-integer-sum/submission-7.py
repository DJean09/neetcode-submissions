class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = 0
        numHash = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in numHash:
                return [numHash[comp], i]
            numHash[nums[i]] = i
        
        return []