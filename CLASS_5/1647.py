import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().rstrip().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
  a, b, c = map(int, input().rstrip().split())
  graph[a].append([b, c])
  graph[b].append([a, c])

q, dist, cnt = [], 0, 0
max_dist = 0
visited = [False for _ in range(v + 1)]
heapq.heappush(q, (0, 1))

while cnt < v:
  d, v2 = heapq.heappop(q)
  if not visited[v2]:
    visited[v2] = True
    dist += d
    cnt += 1
    max_dist = max(max_dist, d)

    for e in graph[v2]:
      if not visited[e[0]]:
        heapq.heappush(q, (e[1], e[0]))

print(dist - max_dist)