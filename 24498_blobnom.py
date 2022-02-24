import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))
highest = max(arr[0], arr[-1])

for i in range(1, n-1):
  height = arr[i] + min(arr[i-1], arr[i+1])
  highest = max(highest, height)

print(highest)