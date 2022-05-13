import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coins = sorted([int(input()) for _ in range(n)])

dp = [0 for _ in range(k+1)]
dp[0] = 1

for i in range(len(coins)):
    for j in range(coins[i], k+1):
        if j-coins[i] >= 0:
            dp[j] += dp[j-coins[i]]

print(dp[-1])