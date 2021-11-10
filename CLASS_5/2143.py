import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
n = int(input())
a = list(map(int, input().rstrip().split()))
m = int(input())
b = list(map(int, input().rstrip().split()))

dic = defaultdict(int)
ans = 0

for i in range(n):
  sum_ = 0
  for j in range(i, n):
    sum_ += a[j]
    dic[sum_] += 1

for i in range(m):
  sum_ = 0
  for j in range(i, m):
    sum_ += b[j]
    ans += dic[T - sum_]

print(ans)
