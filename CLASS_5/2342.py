import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def point(a, b):
  if a == 0:
    return 2
  elif abs(a - b) == 2:
    return 4
  elif a == b:
    return 1
  else:
    return 3

arr = list(map(int, input().rstrip().split()))
length = len(arr) - 1
dp = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(length + 1)]

def solve(n, l, r):
  if n >= length:
    return 0
  elif dp[n][l][r] != -1:
    return dp[n][l][r]
  else:
    dp[n][l][r] = min(solve(n + 1, arr[n], r) + point(l, arr[n]), solve(n + 1, l, arr[n]) + point(r, arr[n]))
    return dp[n][l][r]

print(solve(0, 0, 0))