import sys
import heapq
input = sys.stdin.readline

INF = 1e9

n, e = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().rstrip().split())

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    dist = [INF] * (n+1)
    dist[start] = 0

    while q:
        distance, now = heapq.heappop(q)

        if dist[now] < distance:
            continue

        for v, w in graph[now]:
            if distance + w < dist[v]:
                dist[v] = distance + w
                heapq.heappush(q, (distance + w, v))

    return dist[end]

v1_1 = dijkstra(1, v1)
v2_1 = dijkstra(1, v2)
v1_n = dijkstra(v1, n)
v2_n = dijkstra(v2, n)
v1_v2 = dijkstra(v1, v2)

shortest = min(v1_1 + v1_v2 + v2_n, v2_1 + v1_v2 + v1_n)
print(shortest if shortest < 1e9 else -1)