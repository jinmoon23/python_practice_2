def solutions(graph, start):
  connections = {}
  for curr, next in graph:
    if curr not in connections: connections[curr] = []
    connections[curr].append(next)
  
  def dfs(node, visited, result):
    visited.add(node)
    result.append(node)
    
    neihbors = connections.get(node, [])

    for neighbor in neihbors:
      if (neighbor not in visited):
        dfs(neighbor, visited, result)

  visited, result = set(), []

  dfs(start, visited, result)

  return result  


print(solutions([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A'));
print(solutions([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A'));