class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freqmap = {}

        for num in nums:
            freqmap[num] = 1 + freqmap.get(num, 0)

        heap = []

        for num in freqmap.keys():
            heapq.heappush(heap, (freqmap[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result