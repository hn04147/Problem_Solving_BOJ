import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())

graph = [[] for _ in range(n + 1)]
result = [0]

for _ in range(m):
  a, b = map(int, input().strip().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, n + 1):
  distance = [0 for _ in range(n + 1)]
  visited = [0 for _ in range(n + 1)]
  queue = deque()
  queue.append(i)
  cnt = 0
  sum = 0

  while queue:
    cnt += 1
    for j in range(len(queue)):
      pos = queue.popleft()
      for k in range(len(graph[pos])):
        if visited[graph[pos][k]] == 0:
          visited[graph[pos][k]] = 1
          queue.append(graph[pos][k])
          distance[graph[pos][k]] = cnt
  distance[i] = 0
  
  for j in distance:
    sum += j
  result.append(sum)

print(result.index(min(result[1:])))