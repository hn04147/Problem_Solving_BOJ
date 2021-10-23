import sys
from pprint import pprint
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
k = int(input().rstrip())

graph = [[] for _ in range(n)]
for i in range(n):
  if arr[i] != -1:
    graph[arr[i]].append(i)

def bfs(node):
  q = deque()
  q.append(node)
  while q:
    node = q.popleft()
    if len(graph[node]) != 0:
      for i in graph[node]:
        q.append(i)
      graph[node] = []

bfs(k)

cnt = 0

for i in range(n):
  for j in range(len(graph[i])):
    if len(graph[graph[i][j]]) == 0:
      cnt += 1
print((cnt - 1) if (cnt - 1) != -1 else 0)