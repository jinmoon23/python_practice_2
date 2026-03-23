from collections import deque

def solutions(graph, start):
  mapped = {}
  for st, en in graph:
    if st not in mapped: mapped[st] = []
    mapped[st].append(en)
  
  visited, result = set(), []

  def bfs(node):
    q = deque()
    q.append(node)
    visited.add(node)
    result.append(node)

    while (q):
      poped = q.popleft()
      connected = mapped.get(poped, [])

      for next_node in connected:
        if next_node not in visited:
          q.append(next_node)
          visited.add(next_node)
          result.append(next_node)
    
  bfs(start)
    
  return result

print(solutions([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A'));
print(solutions([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A'));