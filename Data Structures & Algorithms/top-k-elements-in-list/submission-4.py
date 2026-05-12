class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the list
        counts = Counter(nums)

        # look through and return the most frequent
        return [item[0] for item in counts.most_common(k)]