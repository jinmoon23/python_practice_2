import heapq

heap = []

for i in [5,3,10,1]:
  heapq.heappush(heap, i)

print(heap)
print(heapq.heappop(heap))
print(heap)
print(heapq.heappop(heap))