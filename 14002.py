import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))
dp = [1] * n

for i in range(n):
  for j in range(i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j] + 1)

idx = max(dp)
print(idx)

q = []
for i in range(n-1, -1, -1):
  if dp[i] == idx:
    q.append(arr[i])
    idx -= 1

q.reverse()
for i in q:
  print(i, end=' ')