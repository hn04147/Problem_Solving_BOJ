import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))

forward = [1] * n
backward = [1] * n
ans = 0

for i in range(n):
  for j in range(i):
    if arr[i] > arr[j]:
      forward[i] = max(forward[i], forward[j] + 1)

for i in range(n-1, -1, -1):
  for j in range(n-1, i, -1):
    if arr[i] > arr[j]:
      backward[i] = max(backward[i], backward[j] + 1)

result = [i + j - 1 for i, j in zip(forward, backward)]
print(max(result))