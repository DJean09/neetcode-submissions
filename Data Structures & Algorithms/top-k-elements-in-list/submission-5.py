class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the list into a dictionary
        count = Counter(nums)

        # Look through and return the most frequent k
        return [item[0] for item in count.most_common(k)]