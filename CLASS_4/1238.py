import sys
import heapq
input = sys.stdin.readline

INF = 1e9

n, m, x = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().rstrip().split())
    graph[a].append((b, t))

def dijkstra(start, end): # return dist array if end is -1 else return distance from start to end
    q = []
    dist = [INF] * (n+1)
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        distance, now = heapq.heappop(q)

        if distance > dist[now]:
            continue

        for v, w in graph[now]:
            if distance + w < dist[v]:
                dist[v] = distance + w
                heapq.heappush(q, (distance + w, v))

    if end == -1:
        return dist
    else:
        return dist[end]

x_to_others = dijkstra(x, -1)

ans = -1

for i in range(1, n+1):
    if i != x:
        distance = dijkstra(i, x)
        if ans < distance + x_to_others[i]:
            ans = distance + x_to_others[i]

print(ans)