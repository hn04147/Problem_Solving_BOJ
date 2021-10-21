import sys
from collections import deque
from pprint import pprint
import copy
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# if arr exist 0 return True else False
def check_0(arr):
  for i in range(n):
    for j in range(n):
      if arr[i][j] == 0:
        return True
  return False

def bfs(s):
  visited = copy.deepcopy(arr)

  year = 0
  q = deque()
  for pos in s:
    q.append(pos)

  while q:
    year += 1
    for _ in range(len(q)):
      x, y = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
          if visited[nx][ny] == 0 or visited[nx][ny] == 2:
            visited[nx][ny] = -1
            q.append([nx, ny])

  if check_0(visited):
    return -1
  else:
    return year

s = deque()
cnt = 2500

def track():
  global cnt

  if len(s) == m:
    idx = bfs(s)
    if idx != -1:
      cnt = min(cnt, idx)
    return
  else:
    for i in range(n):
      for j in range(n):
        if arr[i][j] == 2:
          s.append([i, j])
          arr[i][j] = -1
          track()
          arr[i][j] = 2
          s.pop()

track()
print((cnt - 1) if cnt != 2500 else -1)