import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[INF for _ in range(n)] for _ in range(n)]

for i in range(n):
  dp[i][i] = 0

for j in range(1, n):
  i = 0
  while (i + j) < n:
    # dp[i][i + j]
    min_ = INF
    for k in range(j):
      min_ = min(min_, dp[i][i + k] + dp[i + k + 1][i + j] + arr[i][0] * arr[i + k][1] * arr[i + j][1])
    dp[i][i + j] = min_
    i += 1

print(dp[0][-1])