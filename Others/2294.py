import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coins = sorted([int(input()) for _ in range(n)])

dp = [k+1 for _ in range(k+1)]
dp[0] = 0

for i in range(len(coins)):
    for j in range(coins[i], k+1):
        dp[j] = min(dp[j], dp[j-coins[i]] + 1)

print(dp[-1] if dp[-1] != k+1 else -1)