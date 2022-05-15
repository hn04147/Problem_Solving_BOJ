import sys
from collections import deque
input = sys.stdin.readline

def D(num):
  return num * 2 if num * 2 < 9999 else (num * 2) % 10000

def S(num):
  return num - 1 if num != 0 else 9999

def L(num):
  return num % 1000 * 10 + num // 1000

def R(num):
  return num % 10 * 1000 + num % 10

T = int(input())
for _ in range(T):
  start, end = map(int, input().strip().split())
  queue =deque()
  queue.append([start, ''])
  visited = [0 for _ in range(10000)]
  visited[start] = 1
  
  while queue:
    idx, oper = queue.popleft()

    if idx == end:
      print(oper)
      break
    else:
      next = D(idx)
      if visited[next] == 0:
        queue.append([next, oper + 'D'])
        visited[next] = 1
      next = S(idx)
      if visited[next] == 0:
        queue.append([next, oper + 'S'])
        visited[next] = 1
      next = L(idx)
      if visited[next] == 0:
        queue.append([next, oper + 'L'])
        visited[next] = 1
      next = R(idx)
      if visited[next] == 0:
        queue.append([next, oper + 'R'])
        visited[next] = 1