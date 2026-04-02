import heapq
def solutions(graph, start):
  distances = {}
  for node in graph:
    distances[node] = float('inf')
  
  distances[start] = 0

  paths = {start : [start]}

  pq = []
  heapq.heappush(pq, [distances[start], start])

  while (pq):
    curr_dist, curr_node = heapq.heappop(pq)
    if distances[curr_node] < curr_dist: continue

    neighbor_nodes = graph[curr_node]
    for node in neighbor_nodes:
      weight = neighbor_nodes[node]
      distance = weight + curr_dist
      
      if distance < distances[node]:
        distances[node] = distance
        heapq.heappush(pq, [distance, node])
        new_path = paths[curr_node] + [node]
        paths[node] = new_path
  
  return [distances, paths]
  

print(solutions({
  'A': {'B': 9, 'C': 3},
  'B': {'A': 5}, 
  'C': {'B': 1}
  }, 'A'))

print(solutions({
  'A': {'B': 1},
  'B': {'C': 5},
  'C': {'D': 1},
  'D': {}
}, 'A'))