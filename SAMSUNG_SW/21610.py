import sys
from collections import deque
import time
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
clouds = deque([[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]])

dxx = [0, -1, -1, -1, 0, 1, 1, 1]
dyy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [-1, 1, 1, -1]
dy = [-1, -1, 1, 1]

for _ in range(m):
  d, s = map(int, input().rstrip().split())

  for _ in range(len(clouds)):
    x, y = clouds.popleft()
    clouds.append([(x + dxx[d-1] * s) % n, (y + dyy[d-1] * s) % n])

  visited = [[False for _ in range(n)] for _ in range(n)]

  for cloud in clouds:
    graph[cloud[0]][cloud[1]] += 1
    visited[cloud[0]][cloud[1]] = True
  
  for cloud in clouds:
    idx = 0
    for i in range(4):
      nx, ny = cloud[0]+dx[i], cloud[1]+dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] > 0:
          idx += 1
    graph[cloud[0]][cloud[1]] += idx

  clouds = deque([])

  for i in range(n):
    for j in range(n):
      if graph[i][j] >= 2 and visited[i][j] == False:
        clouds.append([i, j])
        graph[i][j] -= 2

  print(clouds)

ans = sum([sum(i) for i in graph])
print(ans)