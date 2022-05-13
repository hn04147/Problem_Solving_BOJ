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

# import sys
# input = sys.stdin.readline
# from collections import deque
# from itertools import combinations

# def bfs(q):
#   visited = [[False] * N for _ in range(N)]
#   for x, y in q:
#     visited[x][y] = True
#   time = -1
#   cnt = len(q)
#   while q:
#     for _ in range(len(q)):
#       x, y = q.popleft()
#       for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and not matrix[nx][ny] == 1:
#           visited[nx][ny] = True
#           q.append((nx, ny))
#           cnt += 1
#     time += 1
#   return cnt, time

# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]

# N, M = map(int, input().split())
# matrix = []
# initial_points = []
# wall = 0
# for i in range(N):
#   a = list(map(int, input().split()))
#   for j in range(N):
#     if a[j] == 2:
#       initial_points.append((i,j))
#     elif a[j] == 1:
#       wall += 1
#   matrix.append(a)

# min_count = float('inf')
# for virus_set in combinations(initial_points, M):
#   q = deque()
#   for virus in virus_set:
#     q.append(virus)
#   cnt, time = bfs(q)
#   if cnt + wall == N**2:
#     min_count = min(min_count, time)
# if min_count == float('inf'):
#   min_count = -1
# print(min_count)