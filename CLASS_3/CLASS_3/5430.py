import sys
from collections import deque

n = int(input())
for _ in range(n):
  order = sys.stdin.readline().rstrip()
  number = int(input())
  queue = deque()
  arr = sys.stdin.readline().rstrip()
  if arr != '[]':
    arr = arr[1:-1].split(',')
    for i in arr:
      queue.append(i)
  is_empty = False

  flag = 0
  for i in order:
    if i == 'R':
      flag += 1
    else:
      if queue:
        if flag % 2 == 1:
          queue.reverse()
          queue.popleft()
          flag = 0
        else:
          queue.popleft()
      else:
        print('error')
        is_empty = True
        break

  if not is_empty:
    print('[', end = '')
    for i in range(len(queue)):
      print(queue[i] + (']' if i == (len(queue)- 1) else ','), end = '')
    print('')