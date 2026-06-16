class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Counts how many times each number appears
        count = {}
        for num in nums:
            # Add to the existing value in num
            # hashMap.get(key, default fallback value if empty)
            count[num] = 1 + count.get(num, 0)
        
        # building the heap. import heapq for this.
        heap = []
        for num in count.keys():
            # using heapq to push the values in while sorting them based on frequency.
            heapq.heappush(heap, (count[num], num))
            # Once k has been reached. We pop out the element with the lowest frequency
            if len(heap) > k:
                heapq.heappop(heap)
        
        # pop all the elements from the heap and collect their numbers into the result list
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result