import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

t = int(input())
arr = [list(input().strip()) for _ in range(t)]
cnt_1, cnt_2 = 0, 0
visited = [[False] * t for _ in range(t)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(arr, x, y):
  visited[x][y] = True
  for i in range(4):
    a = x + dx[i]
    b = y + dy[i]
    if 0 <= a < t and 0 <= b < t:
      if arr[a][b] == arr[x][y] and not visited[a][b]:
        dfs(arr, a, b)

for i in range(t):
  for j in range(t):
    if not visited[i][j]:
      cnt_1 += 1
      dfs(arr, i, j)

for i in range(t):
  for j in range(t):
    if arr[i][j] == 'R':
      arr[i][j] = 'G'

visited = [[False] * t for _ in range(t)]
for i in range(t):
  for j in range(t):
    if not visited[i][j]:
      cnt_2 += 1
      dfs(arr, i, j)

print(cnt_1, cnt_2)