import sys
sys.setrecursionlimit(10000)
from collections import deque
input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# nodes = [1 for _ in range(n + 1)]
# for _ in range(m):
#   u, v = map(int, input().split())
#   graph[u].append(v)
#   graph[v].append(u)

# count = 0

# for i in range(len(graph)):
#   if graph[i] and nodes[i] == 1:
#     count += 1
#     queue = deque()
#     queue.append(i)
#     nodes[i] = 0
#     while queue:
#       element = queue.pop()
#       for k in range(len(graph[element])):
#         if nodes[graph[element][k]] == 1:
#           queue.append(graph[element][k])
#           nodes[graph[element][k]] = 0

# print(count)

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
for _ in range(m):
  u, v = map(int, input().split())
  graph[u][v] = 1
  graph[v][u] = 1
count = 0

def dfs(v):
  global visited
  visited[v] = True
  for i in range(1, n + 1):
    if not visited[i] and graph[v][i] == 1:
      dfs(i)

for i in range(1, n + 1):
  if not visited[i]:
    count += 1
    dfs(i)

print(count)