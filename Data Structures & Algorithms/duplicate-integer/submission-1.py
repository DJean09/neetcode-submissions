class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numHash = {}
        num_len = len(nums)

        for i in range(num_len):
            if nums[i] in numHash:
                return True
            numHash[nums[i]] = i
        
        return False