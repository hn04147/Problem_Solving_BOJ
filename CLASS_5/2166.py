import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
arr.append(arr[0])

left, right = 0, 0
for i in range(0, n):
  left += arr[i][0] * arr[i + 1][1]
  right += arr[i][1] * arr[i + 1][0]
print(abs(round((left - right) / 2, 1)))