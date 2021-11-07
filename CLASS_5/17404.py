import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

INF = sys.maxsize
ans = INF

for i in range(3):
  dp = [[0 for _ in range(3)] for _ in range(n)]
  for j in range(3):
    if i == j:
      dp[0][j] = arr[0][j]
    else:
      dp[0][j] = INF

  for j in range(1, n):
    dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + arr[j][0]
    dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + arr[j][1]
    dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + arr[j][2]

  for j in range(3):
    if i != j:
      ans = min(ans, dp[-1][j])

print(ans)