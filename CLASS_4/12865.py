import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
bag = [[0, 0]] + [list(map(int, input().rstrip().split())) for _ in range(n)]
arr = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, k + 1):
    if bag[i][0] > j:
      arr[i][j] = arr[i - 1][j]
    else:
      arr[i][j] = max(arr[i - 1][j], bag[i][1] + arr[i - 1][j - bag[i][0]])
    # arr[i][j] = arr[i - 1][j] if bag[i][0] > j else max(arr[i - 1][j], bag[i][1] + arr[i - 1][j - bag[i][0]])

print(arr[-1][-1])