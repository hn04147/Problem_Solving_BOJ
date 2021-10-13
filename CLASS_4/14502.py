import sys
import copy
from pprint import pprint
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(m)]

# find virus
virus = []
for i in range(m):
  for j in range(n):
    if arr[i][j] == 2:
      virus.append([i, j])

def bfs(arr):
  graph = copy.deepcopy(arr)
  global virus
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]

  q = deque()
  for v in virus:
    q.append(v)

  while q:
    v = q.popleft()
    for i in range(4):
      x = v[0] + dx[i]
      y = v[1] + dy[i]
      if 0 <= x < m and 0 <= y < n:
        if graph[x][y] == 0:
          q.append([x, y])
          graph[x][y] = 2
  
  cnt = 0
  for i in graph:
    for j in i:
      if j == 0:
        cnt += 1

  return cnt

max_empty = 0

def wall(cnt):
  global max_empty

  if cnt == 3:
    max_empty = max(max_empty, bfs(arr))
    return
  else:
    for i in range(m):
      for j in range(n):
        if arr[i][j] == 0:
          arr[i][j] = 1
          wall(cnt + 1)
          arr[i][j] = 0

wall(0)
print(max_empty)