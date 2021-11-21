import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
graph = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
  graph[i][i] = 0
for _ in range(m):
  a, b, c = map(int, input().rstrip().split())
  graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c)

for k in range(n):
  for i in range(n):
    for j in range(n):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
  for j in range(n):
    print(f'{graph[i][j] if graph[i][j] != INF else 0} ', end = '')
  print()