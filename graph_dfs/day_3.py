def solutions(graph, start):
  mapped = {}
  for st, en in graph:
    if st not in mapped: mapped[st] = []
    mapped[st].append(en)
  
  visited, result = set(), []

  def dfs(node):
    visited.add(node)
    result.append(node)
    connected = mapped.get(node, [])
    for next_node in connected:
      if next_node not in visited: dfs(next_node)

  dfs(start)

  return result


print(solutions([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A'));
print(solutions([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A'));