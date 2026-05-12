class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # using set() works much faster for handling unique numbers
        # sets better for single values, dict is better for pairs
        seen = set()

        # no need for the list length
        # iterate through and add to seen if not there already
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        
        # return false if nothing was found
        return False