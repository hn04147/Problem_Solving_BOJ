import sys
import math
from pprint import pprint
input = sys.stdin.readline

INF = math.inf
n, m = map(int, input().rstrip().split())
graph = []
distance = [INF for _ in range(n + 1)]
distance[1] = 0

for _ in range(m):
  i, j, k = map(int, input().rstrip().split())
  graph.append([i, j, k])

for _ in range(n - 1):
  for info in graph:
    i, j, k = info
    if distance[i] != INF:
      distance[j] = min(distance[j], distance[i] + k)

distance_1 = distance[2:]

for _ in range(n - 1):
  for info in graph:
    i, j, k = info
    if distance[i] != INF:
      distance[j] = min(distance[j], distance[i] + k)

distance_2 = distance[2:]

if distance_1 == distance_2:
  for d in distance_1:
    print(d if d != INF else -1)
else:
  print(-1)