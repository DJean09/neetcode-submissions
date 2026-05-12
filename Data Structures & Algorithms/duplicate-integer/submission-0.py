class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap = {}
        num_len = len(nums)

        for i in range(num_len):
            if nums[i] in numMap:
                return True
            
            numMap[nums[i]] = i
        
        return False