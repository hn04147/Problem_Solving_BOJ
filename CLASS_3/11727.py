n = int(input())
dp = [0, 1, 3, 5]
if n <= 3:
  print(dp[n])
else:
  for i in range(4, n + 1):
    dp.append(dp[i - 2] * 2 + dp[i - 1])
  print(dp[n] % 10007)