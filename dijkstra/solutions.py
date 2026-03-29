class MinHeap:
  def __init__(self):
    self.items = []
  
  def size(self):
    return len(self.items)
  
  def push(self, item):
    self.items.append(item)
    self.bubbleUp()
  
  def pop(self):
    min = self.items[0]
    self.items[0] = self.items[self.size() - 1]
    self.items.pop()
    self.bubbleDown()
    return min
  
  def swap(self, a, b):
    self.items[a], self.items[b] = self.items[b], self.items[a]
  
  def bubbleUp(self):
    index = self.size() - 1

    while (index > 0):
      parentIndex = (index - 1) // 2
      if self.items[parentIndex] <= self.items[index]: break
      self.swap(index, parentIndex)
      index = parentIndex
  
  def bubbleDown(self):
    index = 0

    while (index * 2 + 1 < self.size()):
      left_child, right_child = index * 2 + 1, index * 2 + 2
      smaller_child = left_child
      if right_child < self.size() and self.items[right_child] < self.items[left_child]:
        smaller_child = right_child
      if self.items[index] <= self.items[smaller_child]: break
      self.swap(index, smaller_child)
      index = smaller_child
  

def solutions(graph, start):
  distances = {}
  for node in graph:
    distances[node] = float('inf')
  
  distances[start] = 0

  paths = {start : [start] }

  q = MinHeap()
  q.push([start, distances[start]])

  while (q.size() > 0):
    curr_node, curr_dist = q.pop()
    if distances[curr_node] < curr_dist: continue
    
    neigbor_nodes = graph[curr_node]
    for node in neigbor_nodes:
      weight = neigbor_nodes[node]
      distance = weight + curr_dist
      if distance < distances[node]:
        distances[node] = distance
        q.push([node, distance])
        newPath = paths[curr_node] + [node]
        paths[node] = newPath
  
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