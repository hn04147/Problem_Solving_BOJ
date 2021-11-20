import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
dp = [[False for _ in range(n)] for _ in range(n)]

for j in range(n):
  for i in range(j + 1):
    if i == j:
      dp[i][j] = True
    else:
      if arr[i] == arr[j]:
        if j - i == 1:
          dp[i][j] = True
        else:
          if dp[i + 1][j - 1] == True:
            dp[i][j] = True

t = int(input())
for _ in range(t):
  a, b = map(int, input().rstrip().split())
  print(1 if dp[a - 1][b - 1] == True else 0)