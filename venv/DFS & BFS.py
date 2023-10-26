graph = {
  'A' : ['B', 'C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = []  # List to keep track of visited nodes.
queue = []    # Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  print("BFS : ")
  while queue:
    s = queue.pop(0)
    print(s, end=" ")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

bfs(visited, graph, 'A')

# Now, using uppercase keys in the graph
graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': []
}

visited = []  # List to keep track of visited nodes
print("\nDFS : " )
def dfs(visited, graph, node):
  if node not in visited:
    print(node, end = " ")
    visited.append(node)
    for neighbour in graph[node]:
      dfs(visited, graph, neighbour)

dfs(visited, graph, 'A')
