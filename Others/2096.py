import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))

min_arr = []
max_arr = []
for i in range(3):
  min_arr.append(arr[i])
  max_arr.append(arr[i])

for i in range(1, n):
  arr = list(map(int, input().rstrip().split()))

  min_idx = [0, 0, 0]
  max_idx = [0, 0, 0]

  min_idx[0] = min(min_arr[0], min_arr[1]) + arr[0]
  min_idx[1] = min(min_arr) + arr[1]
  min_idx[2] = min(min_arr[1], min_arr[2]) + arr[2]

  max_idx[0] = max(max_arr[0], max_arr[1]) + arr[0]
  max_idx[1] = max(max_arr) + arr[1]
  max_idx[2] = max(max_arr[1], max_arr[2]) + arr[2]

  for j in range(3):
    min_arr[j] = min_idx[j]
    max_arr[j] = max_idx[j]

print(max(max_arr), min(min_arr))