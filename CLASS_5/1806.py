import sys
input = sys.stdin.readline

n, s = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

min_len = 100001
l, r = 0, 0
tmp_sum = arr[0]

while True:
  if tmp_sum >= s:
    min_len = min(min_len, r - l + 1)
    tmp_sum -= arr[l]
    l += 1
  else:
    r += 1
    if r == n:
      break
    tmp_sum += arr[r]

print(0 if min_len == 100001 else min_len)