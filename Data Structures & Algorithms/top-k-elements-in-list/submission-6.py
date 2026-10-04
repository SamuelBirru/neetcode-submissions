class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)
        
        heap = []
        
        for num in hashmap.keys():
            heapq.heappush(heap, (hashmap[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for num in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
                        

        