from collections import deque

a, b = map(int, input().split())

def oper_1(n):
  return n * 2

def oper_2(n):
  return n * 10 + 1

visited = [a]
_continue = True
cnt = 0
queue = deque()
queue.append(a)

while _continue:
  cnt += 1
  for _ in range(len(queue)):
    n = queue.popleft()
    if n == b:
      _continue = False
      break
    else:
      x, y = oper_1(n), oper_2(n)
      if x not in visited and x <= b:
        queue.append(x)
        visited.append(x)
      if y not in visited and y <= b:
        queue.append(y)
        visited.append(y)
  if not _continue:
    break
  if not queue:
    break

print(cnt if not _continue else -1)