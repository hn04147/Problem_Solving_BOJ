import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
  n = int(input().strip())
  arr = [list(map(int, input().strip().split())) for _ in range(2)]
  
  dp = [[0] * n for _ in range(2)]
  dp[0][0], dp[1][0] = arr[0][0], arr[1][0]
  if n == 1:
    print(max(dp[0][0], dp[1][0]))
  elif n == 2:
    print(max(arr[0][0] + arr[1][1], arr[0][1] + arr[1][0]))
  else:
    dp[0][1], dp[1][1] = dp[1][0] + arr[0][1], dp[0][0] + arr[1][1]
    for i in range(2, n):
      for j in range(2):
        dp[j][i] = arr[j][i] + max(dp[0][i - 2], dp[1][i - 2], dp[0 if j == 1 else 1][i - 1])
    print(max(dp[0][-1], dp[0][-2], dp[1][-1], dp[1][-2]))