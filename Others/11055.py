import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))
sums = arr[:]

for i in range(n):
  for j in range(i):
    if arr[i] > arr[j]:
      sums[i] = max(sums[i], sums[j] + arr[i])

print(max(sums))