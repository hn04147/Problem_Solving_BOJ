import sys
import heapq
import math
input = sys.stdin.readline

def distance(a, b):
  return round(math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2), 2)

n = int(input())
arr = [list(map(float, input().rstrip().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
for i in range(n - 1):
  for j in range(i + 1, n):
    distance_ = distance(arr[i], arr[j])
    graph[i].append([j, distance_])
    graph[j].append([i, distance_])


q = []
dist = 0
cnt = 0
visited = [False for _ in range(n)]
heapq.heappush(q, (0, 0))

while cnt < n:
  d, v = heapq.heappop(q)
  if not visited[v]:
    visited[v] = True
    dist += d
    cnt += 1

    for e in graph[v]:
      if not visited[e[0]]:
        heapq.heappush(q, (e[1], e[0]))

print(dist)