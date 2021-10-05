import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))
cnt = [1] * n

for i in range(1, n):
  for j in range(0, i):
    if arr[i] > arr[j]:
      cnt[i] = max(cnt[i], cnt[j] + 1)

print(max(cnt))