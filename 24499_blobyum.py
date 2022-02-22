import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
pies = list(map(int, input().rstrip().split()))

l, r = 0, k - 1
sum_ = sum(pies[l:r+1])
max_sum = sum_

for _ in range(n - 1):
  l += l
  r = r + 1 if r + 1 < n else (r + 1) % n
  sum_ = sum_ - pies[l-1] + pies[r]
  max_sum = max(max_sum, sum_)

print(max_sum)