import sys
input = sys.stdin.readline
from pprint import pprint
from collections import deque

arr = [list(input().rstrip()) for _ in range(12)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

while True:
  exist = False
  visited = [[0] * 6 for _ in range(12)]

  for i in range(11, -1, -1):
    for j in range(6):
      in_q = []
      if arr[i][j] != '.' and visited[i][j] == 0:
        q = deque()
        q.append([i, j])
        visited[i][j] = 1
        in_q.append([i, j])
        while q:
          x, y = q.popleft()
          for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 12 and 0 <= ny < 6:
              if arr[nx][ny] == arr[x][y] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                in_q.append([nx, ny])
                q.append([nx, ny])
      if len(in_q) >= 4:
        if not exist:
          exist = True
        for x, y in in_q:
          arr[x][y] = '.'

  if not exist:
    break
  else:
    cnt += 1

  # for j in range(6):
  #   col_arr = []
  #   for i in range(12):
  #     col_arr.append(arr[i][j])
  #   if 'R' in col_arr or 'G' in col_arr or 'B' in col_arr or 'P' in col_arr or 'Y' in col_arr:
  #     for _ in range(11):

  arr_ = [['.'] * 6 for _ in range(12)]
  for j in range(6):
    idx = 11
    for i in range(11, -1, -1):
      if arr[i][j] != '.':
        arr_[idx][j] = arr[i][j]
        idx -= 1
  for i in range(12):
    for j in range(6):
      arr[i][j] = arr_[i][j]
  
  pprint(arr)

print(cnt)