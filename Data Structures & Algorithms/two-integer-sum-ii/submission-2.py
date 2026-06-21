class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initialize the pointers
        l, r = 0, len(numbers) - 1

        while l < r:
            currentSum = numbers[l] + numbers[r]

            # because its already sorted if the sum is greater than target we lower the bigger number
            if currentSum > target:
                r -= 1
            elif currentSum < target:
                # if lower than target, then we increase the smaller number
                l += 1
            else:
                return [l + 1, r + 1]
        
        # return empty if nothing matches
        return []