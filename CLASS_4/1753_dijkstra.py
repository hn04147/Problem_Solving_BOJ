import sys
import math
import heapq
input = sys.stdin.readline
INF = math.inf

n, m = map(int, input().strip().split())
start = int(input().strip())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  this_node, next_node, weight = map(int, input().strip().split())
  graph[this_node].append((weight, next_node))
dist = [INF] * (n + 1)
heap = []

def dijkstra(start):
  dist[start] = 0
  heapq.heappush(heap, (0, start))

  while heap:
    weight, now = heapq.heappop(heap)

    if dist[now] < weight:
      continue
    else:
      for w, next_node in graph[now]:
        next_weight = weight + w
        if next_weight < dist[next_node]:
          dist[next_node] = next_weight
          heapq.heappush(heap, (next_weight, next_node))

dijkstra(start)
for i in range(1, len(dist)):
  print('INF' if math.isinf(dist[i]) else dist[i])







# n, m = map(int, input().strip().split())
# start = int(input().strip())
# arr = [[0] * (n + 1) for _ in range(n + 1)]
# for _ in range(m):
#   a, b, c = map(int, input().strip().split())
#   arr[a][b] = c

# def dijkstra(arr, start, n):
#   distance = [math.inf] * (n + 1)
#   distance[start] = 0

#   for _ in range(n - 1):
#     for i in range(1, n + 1):
#       for j in range(1, n + 1):
#         if j != start:
#           if arr[i][j] != 0:
#             distance[j] = min(distance[j], distance[i] + arr[i][j])
  
#   for i in range(1, len(distance)):
#     print('INF' if math.isinf(distance[i]) else distance[i])

# dijkstra(arr, start, n)