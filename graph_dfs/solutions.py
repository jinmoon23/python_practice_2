def solutions(graph, start):
  relations = {}
  for prev, next in graph:
    if prev not in relations: relations[prev] = [next]
    else: relations[prev].append(next)

  def dfs(node, visited, result):
    visited.add(node)
    result.append(node)
    neigbors = relations.get(node, [])
    for neigbor in neigbors:
      if neigbor not in visited:
        dfs(neigbor, visited, result)
  
  visited, result = set(), []

  dfs(start, visited, result)
  
  return result
      

print(solutions([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A'));
print(solutions([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A'));