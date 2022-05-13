import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))
ans = [-1] * n

for i in range(n-2, -1, -1):
  if arr[i] != arr[i+1]:
    ans[i] = i+2
  else:
    ans[i] = ans[i+1]

print(*ans)