class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        num_len = len(nums)

        for i in range(num_len):
            total = 1

            for j in range(num_len):
                if j != i:
                    total = total * nums[j]
            
            res.append(total)
        
        return res