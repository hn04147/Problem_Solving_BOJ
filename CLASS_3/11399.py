import sys
input = sys.stdin.readline

n = int(input().strip())
arr = sorted(list(map(int, input().strip().split())))
result = []
result.append(arr[0])
answer = arr[0]

for i in range(1, n):
  result.append(arr[i] + result[i - 1])
  answer += result[i]
print(answer)