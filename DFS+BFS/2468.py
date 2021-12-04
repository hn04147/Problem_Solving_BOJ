import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

def bfs(num):
  visited = [[False for _ in range(n)] for _ in range(n)]
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]
  cnt = 0

  for i in range(n):
    for j in range(n):
      if not visited[i][j] and (arr[i][j] - num) > 0:
        visited[i][j] = True
        q = deque([[i, j]])
        cnt_idx = 1
        while q:
          for _ in range(len(q)):
            x, y = q.popleft()
            for k in range(4):
              nx = x + dx[k]
              ny = y + dy[k]
              if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and (arr[nx][ny] - num) > 0:
                  visited[nx][ny] = True
                  q.append([nx, ny])
                  cnt_idx += 1
        cnt += 1

  return cnt

max_num = 0
height = 0

while True:
  result = bfs(height)
  if result == 0:
    print(max_num)
    break
  max_num = max(max_num, result)
  height += 1