import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
prefix_sum = [0]

# for i in range(1, len(arr) + 1):
#   prefix_sum.append(prefix_sum[i - 1] + arr[i - 1])

temp = 0
for i in arr:
  temp += i
  prefix_sum.append(temp)

for i in range(m):
  a, b = map(int, input().strip().split())
  print(prefix_sum[b] - prefix_sum[a - 1])