import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))
b, c = map(int, input().rstrip().split())

result = 0
for num in arr:
  if b >= num:
    result += 1
  else:
    if (num - b) % c == 0:
      result += (1 + (num - b) // c)
    else:
      result += (2 + (num - b) // c)

print(result)