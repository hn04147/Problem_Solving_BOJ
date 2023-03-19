import sys
import heapq
input = sys.stdin.readline

INF = 1e9

n = int(input().rstrip())
m = int(input().rstrip())
# n, m, s, f = 5, 8, 1, 5
# dummy = [[1, 2, 2], [1, 3, 3], [1, 4, 1], [1, 5, 10], [2, 4, 2], [3, 4, 1], [3, 5, 1], [4, 5, 3]]

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
dist = [INF] * (n+1)
previous = [0] * (n+1)

# for u, v, w in dummy:
#     graph[u].append((v, w))

for _ in range(m):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((v, w))
s, f = map(int, input().rstrip().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        distance, now = heapq.heappop(q)

        if dist[now] < distance:
            continue

        for v, w in graph[now]:
            if distance + w < dist[v]:
                dist[v] = distance + w
                previous[v] = now
                heapq.heappush(q, (distance + w, v))

dijkstra(s)

print(dist[f])

city_num = 2
city_list = [f]

while previous[f] != s:
    city_num += 1
    f = previous[f]
    city_list.append(f)

city_list.append(s)

print(city_num)
print(*city_list[::-1])