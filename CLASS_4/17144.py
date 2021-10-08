import sys
from pprint import pprint
input = sys.stdin.readline

m, n, t = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(m)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
machine = []

# position of circulation machine
for i in range(m):
  for j in range(n):
    if arr[i][j] == -1:
      machine.append([i, j])

for _ in range(t):
  # diffusion
  idx_ = [[0] * (n) for _ in range(m)]
  for i in range(m):
    for j in range(n):
      if arr[i][j] == -1:
        idx_[i][j] = -1
      else:
        cnt = 0
        for k in range(4):
          x = i + dx[k]
          y = j + dy[k]
          if 0 <= x < m and 0 <= y < n:
            if arr[x][y] != -1:
              idx_[x][y] += arr[i][j] // 5
              cnt += 1
        idx_[i][j] += (arr[i][j] - (arr[i][j] // 5) * cnt)
  arr = idx_

  # circulation
  # upper circulation
  idx = arr[machine[0][0]][0]
  for i in range(machine[0][0], 0, -1):
    arr[i][0] = arr[i - 1][0] if arr[i][0] != -1 else arr[i][0]
  for i in range(0, n - 1):
    arr[0][i] = arr[0][i + 1]
  for i in range(0, machine[0][0]):
    arr[i][n - 1] = arr[i + 1][n - 1] if arr[i + 1][n - 1] != -1 else 0
  for i in range(n - 1, 0, -1):
    arr[machine[0][0]][i] = arr[machine[0][0]][i - 1] if arr[machine[0][0]][i - 1] != -1 else 0
  arr[machine[0][0]][0] = idx

  # down circulation
  idx = arr[machine[1][0]][0]
  for i in range(machine[1][0], n - 2):
    arr[i][0] = arr[i + 1][0] if arr[i][0] != -1 else arr[i][0]
  for i in range(0, n - 1):
    arr[m - 1][i] = arr[m - 1][i + 1]
  for i in range(m - 1, machine[1][0], -1):
    arr[i][n - 1] = arr[i - 1][n - 1] if arr[i - 1][n - 1] != -1 else 0
  for i in range(n - 1, 0, -1):
    arr[machine[1][0]][i] = arr[machine[1][0]][i - 1] if arr[machine[1][0]][i - 1] != -1 else 0
  arr[machine[1][0]][0] = idx

  # set -1 as circulation machine
  arr[machine[0][0]][machine[0][1]] = arr[machine[1][0]][machine[1][1]] = -1

# sum of tiny dust
sum = 0
for i in range(m):
  for j in range(n):
    sum += arr[i][j]

print(sum + 2)