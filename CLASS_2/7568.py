import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

for i in arr:
  count = 0
  for j in arr:
    if i[0] < j[0] and i[1] < j[1]:
      count += 1
  print(str(count + 1) + ' ', end = '')