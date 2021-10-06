import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr = [[0] * (n + 1)]
for _ in range(n):
  arr.append([0] + list(map(int, input().strip().split())))
sum_ = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, n + 1):
    sum_[i][j] = arr[i][j] + sum_[i - 1][j] + sum_[i][j - 1] - sum_[i - 1][j - 1]

for _ in range(m):
  x1, y1, x2, y2 = map(int, input().strip().split())

  print(sum_[x2][y2] - sum_[x1 - 1][y2] - sum_[x2][y1 - 1] + sum_[x1 - 1][y1 - 1])