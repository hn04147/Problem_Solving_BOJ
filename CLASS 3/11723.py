import sys
input = sys.stdin.readline

n = int(input())
arr = set([])

for _ in range(n):
  order = input().strip().split()
  if order[0] == 'all':
    arr = set([i for i in range(1, 21)])
  elif order[0] == 'empty':
    arr = set([])
  else:
    a, num = order[0], int(order[1])
    if a == 'add':
      arr.add(num)
    elif a == 'remove':
      arr.remove(num)
    elif a == 'check':
      print(1 if num in arr else 0)
    else:
      arr.remove(num) if num in arr else arr.add(num)