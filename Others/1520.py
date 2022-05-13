import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline
sys.setrecursionlimit(10000)

m, n = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(m)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[-1] * n for _ in range(m)]

def track(x, y):
  if x == (m - 1) and y == (n - 1):
    return 1
  if visited[x][y] != -1:
    return visited[x][y]
  visited[x][y] = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < m and 0 <= ny < n:
      if arr[nx][ny] < arr[x][y]:
        visited[x][y] += track(nx, ny)
  return visited[x][y]

print(track(0, 0))