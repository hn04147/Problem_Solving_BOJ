import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline
sys.setrecursionlimit(10000)

m, l, r = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(m)]
visited = [[0] * m for _ in range(m)]
q = deque()
year = 0
cnt = 0
people = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
moved = False

def dfs(x, y):
  global people, cnt, moved

  visited[x][y] = 1
  people += arr[x][y]
  cnt += 1
  q.append([x, y])

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < m and 0 <= ny < m:
      if visited[nx][ny] == 0:
        if l <= abs(arr[x][y] - arr[nx][ny]) <= r:
          if not moved:
            moved = True
          dfs(nx, ny)

def move():
  one_country = people // cnt
  while q:
    x, y = q.pop()
    arr[x][y] = one_country

if __name__ == '__main__':
  while True:
    visited = [[0] * m for _ in range(m)]
    for i in range(m):
      for j in range(m):
        if visited[i][j] == 0:
          people = 0
          cnt = 0
          q = deque()
          dfs(i, j)
          if len(q) > 1:
            move()
    # print(*arr, sep = '\n')

    if moved:
      year += 1
      moved = False
    else:
      break

  print(year)