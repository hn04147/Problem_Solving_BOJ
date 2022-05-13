import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
graph = [[] for _ in range(m+1)]
in_degree = [0] * (m+1)
for _ in range(n):
  a, b = map(int, input().rstrip().split())
  graph[a].append(b)
  in_degree[b] += 1

# answer = []
# dq = deque([])
# visited = [False] * (m+1)
# visited[0] = True

# while not (False not in visited and len(dq) == 0):
#   if len(dq) > 0:
#     a = dq.popleft()
#     answer.append(a)
#     for i in graph[a]:
#       if visited[i] == False and in_degree[i] > 0:
#         in_degree[i] -= 1

#   for i in range(1, m+1):
#     if visited[i] == False and in_degree[i] == 0:
#       visited[i] = True
#       dq.append(i)
  
# print(*answer)

dq = deque()

for i in range(1, m+1):
  if in_degree[i] == 0:
    dq.append(i)

while dq:
  a = dq.popleft()
  for i in graph[a]:
    in_degree[i] -= 1
    if in_degree[i] == 0:
      dq.append(i)
  print(a, end=' ')