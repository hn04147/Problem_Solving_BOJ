import sys
input = sys.stdin.readline

n = int(input().strip())
t = int(input().strip())
arr = input().strip()

target = 'I'
for _ in range(n):
  target += 'OI'

cnt = 0
idx = 0
while idx < t - 2 * n - 1:
  if arr[idx:idx + 2*n + 1] == target:
    cnt += 1
    idx += 2
  else:
    idx += 1

print(cnt)