class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize result array with all values set to 1
        res = [1] * (len(nums))

        # create prefix
        prefix = 1

        # first pass, left to right
        # for each index i
        for i in range(len(nums)):
            # set result[i] = prefix
            # product of all the elements to the left
            res[i] = prefix

            # update prefix *= nums[i]
            prefix *= nums[i]
        
        # create postfix
        postfix = 1

        # second pass, right to left
        # for each index i
        for i in range(len(nums) -1, -1, -1):
            # multiply result[i] by postfix
            # product of all elements to the right
            res[i] *= postfix

            # update postfix
            postfix *= nums[i]
        
        # return result
        return res