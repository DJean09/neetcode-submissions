class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = 0
        hashMap = {}
        num_len = len(nums)

        for i in range(num_len):
            comp = target - nums[i]
            if comp in hashMap:
                return [hashMap[comp], i]
            hashMap[nums[i]] = i
        
        return []