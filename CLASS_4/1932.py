import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(n)]
answer = [[0] * n for _ in range(n)]

for i in range(n):
  for j in range(i + 1):
    if i == j == 0:
      answer[i][j] = arr[i][j]
    else:
      if j > 0:
        answer[i][j] = answer[i - 1][j - 1] + arr[i][j]
      if j < i:
        answer[i][j] = max(answer[i][j], answer[i - 1][j] + arr[i][j])

print(max(answer[-1]))