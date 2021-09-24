import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
arr = list(map(int, input().split()))
count = abs(n - 100)

for i in range(n * 2):
  j = str(i)
  enable = True
  for k in j:
    if int(k) in arr:
      enable = False
      break
  if enable:
    count = min(count, len(str(i)) + abs(i - n))

print(count)