import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
l, r = 0, n - 1
max_ = sys.maxsize
ans = []

while l != r:
  if abs(arr[l] + arr[r]) < max_:
    max_ = abs(arr[l] + arr[r])
    ans = [l, r]
  if arr[l] + arr[r] < 0:
    l += 1
  else:
    r -= 1

print(arr[ans[0]], arr[ans[1]])