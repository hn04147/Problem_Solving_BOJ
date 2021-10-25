import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(m)]

dp = [[0] * n for _ in range(m)]
for i in range(m):
  dp[i][0] = arr[i][0]

for j in range(1, n):
  for i in range(m):
    max_value = 0
    for k in range(m):
      if i == k:
        max_value = max(dp[k][j - 1] + arr[i][j] // 2, max_value)
      else:
        max_value = max(dp[k][j - 1] + arr[i][j], max_value)
    dp[i][j] = max_value

col_arr = []
for i in range(m):
  col_arr.append(dp[i][n - 1])

print(max(col_arr))