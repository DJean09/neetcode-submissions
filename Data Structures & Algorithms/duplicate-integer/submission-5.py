class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        num_len = len(nums)

        for i in range(num_len):
            if nums[i] in seen:
                return True
            seen.add(nums[i])

        return False