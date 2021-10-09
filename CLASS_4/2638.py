import sys
from pprint import pprint
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(m)]

def check_finish():
  for i in arr:
    if 1 in i:
      return False
  return True

cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
  if check_finish():
    break

  cnt += 1
  visited = [[0] * n for _ in range(m)]
  q = deque([])
  q.append([0, 0])

  while q:
    pos_x, pos_y = q.popleft()
    for k in range(4):
      x = pos_x + dx[k]
      y = pos_y + dy[k]
      if 0 <= x < m and 0 <= y < n:
        if arr[x][y] == 0: 
          if visited[x][y] == 0:
            visited[x][y] = 1
            q.append([x, y])
        else:
          arr[x][y] += 1

  for i in range(m):
    for j in range(n):
      arr[i][j] = 0 if (arr[i][j] >= 3 or arr[i][j] == 0) else 1

print(cnt)