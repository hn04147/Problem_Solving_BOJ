import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
arr = []
for _ in range(n):
  arr.insert(0, int(input().strip()))

cnt = 0
for i in arr:
  cnt += k // i
  k %= i

print(cnt)