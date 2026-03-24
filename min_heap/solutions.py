import heapq

heap = []
for x in [5, 3, 10, 1]:
  heapq.heappush(heap, x)

print(heapq.heappop(heap))
print(heapq.heappop(heap))