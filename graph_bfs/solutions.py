from collections import deque

def solutions(graph, start):
  connections = {}
  for curr, nxt in graph:
    if curr not in connections: connections[curr] = []
    connections[curr].append(nxt)
  
  def bfs(node):
    q = deque()
    q.append(node)
    visited.add(node)
    result.append(node)

    while(q):
      current = q.popleft()

      neighbors = connections.get(current, [])

      for neighbor in neighbors:
        if neighbor not in visited:
          q.append(neighbor)
          visited.add(neighbor)
          result.append(neighbor)

  visited, result = set(), []

  bfs(start)

  return result


print(solutions([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A'));
print(solutions([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A'));