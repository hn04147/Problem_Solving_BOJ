n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(graph, start_node):
  visit = list()
  stack = list()
  
  stack.append(start_node)

  while stack:
    node = stack.pop()
    if node not in visit:
      visit.append(node)
      stack.extend(graph[node])
  
  for i in visit:
    print("{} ".format(i), end='')
  print()

def bfs(graph, start_node):
  visit = list()
  queue = list()

  queue.append(start_node)

  while queue:
    node = queue.pop(0)
    if node not in visit:
      visit.append(node)
      queue.extend(graph[node])
      
  for i in range(len(visit)):
    print(visit[i], end = '')

dfs(graph, v)
bfs(graph, v)