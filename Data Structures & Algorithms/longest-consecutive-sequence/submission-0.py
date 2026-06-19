class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert the list into a set for O(1) lookups
        numSet = set(nums)

        # track the length of the longest sequence
        longest = 0

        for num in numSet:
            # chek if num - 1 is not in the set
            # if true, num is the start of a sequence
            if (num - 1) not in numSet:
                # initialize length
                length = 1

                while (num + length) in numSet:
                    length += 1
                
                # updated the longest
                # max() compares length and current longest to see which is bigger
                longest = max(length, longest)
        
        return longest