import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
arr = [input().rstrip() for _ in range(m)]

visited = [0] * 26
visited[ord(arr[0][0]) - 65] = 1
cnt = 1
max_cnt = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
s = deque()
s.append([0, 0])

def track(pos, cnt):
  global max_cnt

  for i in range(4):
    x = pos[0] + dx[i]
    y = pos[1] + dy[i]
    if 0 <= x < m and 0 <= y < n:
      if visited[ord(arr[x][y]) - 65] == 1:
        max_cnt = max(max_cnt, cnt)
      else:
        visited[ord(arr[x][y]) - 65] = 1
        track([x, y], cnt + 1)
        visited[ord(arr[x][y]) - 65] = 0

track([0, 0], cnt)
print(max_cnt)