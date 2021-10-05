import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
answer = [0] * (n + 1)

for _ in range(n - 1):
  a, b = map(int, input().strip().split())
  graph[a].append(b)
  graph[b].append(a)

queue = deque()
queue.append(1)

while queue:
  node = queue.popleft()
  for i in graph[node]:
    if answer[i] == 0:
      answer[i] = node
      queue.append(i)

for i in range(2, n + 1):
  print(answer[i])