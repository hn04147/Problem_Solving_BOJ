import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(m)]
year = 0

def one_year():
  global year, arr
  arr_ = [[0] * n for _ in range(m)]

  for i in range(1, m - 1):
    for j in range(1, n - 1):
      arr_[i][j] = arr_[i][j] + (1 if arr[i - 1][j] == 0 else 0)
      arr_[i][j] = arr_[i][j] + (1 if arr[i][j + 1] == 0 else 0)
      arr_[i][j] = arr_[i][j] + (1 if arr[i + 1][j] == 0 else 0)
      arr_[i][j] = arr_[i][j] + (1 if arr[i][j - 1] == 0 else 0)
  
  for i in range(1, m - 1):
    for j in range(1, n - 1):
      arr[i][j] = arr[i][j] - arr_[i][j] if (arr[i][j] - arr_[i][j]) >= 0 else 0

def count():
  global arr
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]
  visited = [[0] * n for _ in range(m)]
  cnt = 0
  exist = False

  for i in range(1, m):
    for j in range(1, n):
      if arr[i][j] != 0 and visited[i][j] == 0:
        if exist == False:
          exist = True
        cnt += 1
        visited[i][j] = 1
        q = deque()
        q.append([i, j])
        while q:
          x_, y_ = q.popleft()
          for k in range(4):
            x = x_ + dx[k]
            y = y_ + dy[k]
            if arr[x][y] != 0 and visited[x][y] == 0:
              visited[x][y] = 1
              q.append([x, y])
  if exist == False:
    return -1
  else:
    return cnt

while True:
  one_year()
  year += 1
  if count() == -1:
    year = 0
    break
  elif count() > 1:
    break

print(year)