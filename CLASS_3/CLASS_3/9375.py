import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  m = int(input())
  dic = {}
  for _ in range(m):
    name, type = input().strip().split()
    if type in dic:
      dic[type] += 1
    else:
      dic[type] = 1

  answer = 1
  for key in dic:
    answer *= dic[key] + 1
  print(answer - 1)