import sys
import math
input = sys.stdin.readline
INF = math.inf

N = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        graph[i][j] = INF if graph[i][j] == 0 else graph[i][j]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != k and j != k:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(N):
    for j in range(N):
        graph[i][j] = 0 if graph[i][j] == INF else 1
    print(*graph[i])