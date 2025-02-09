import heapq

# create a heap
heap = []

# this will automatically create a minHeap
heapq.heapify(heap)

nums = [1, 4, 6, 24, 7]

for num in nums:
    heapq.heappush(heap, num)
    
print(heap)
print(heapq.heappop(heap))