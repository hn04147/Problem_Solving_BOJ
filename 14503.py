import sys
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
r, c, dir = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(m)]

cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def n_dir(n):
  return (n + 3) % 4

def b_dir(n):
  return (n + 2) % 4

def clean(x, y, d):
  global cnt

  if arr[x][y] == 0:
    arr[x][y] = 2
    cnt += 1

  for _ in range(4):
    nd = n_dir(d)
    nx = x + dx[nd]
    ny = y + dy[nd]
    if arr[nx][ny] == 0:
      clean(nx, ny, nd)
      return
    d = nd
  
  nd = b_dir(d)
  nx = x + dx[nd]
  ny = y + dy[nd]
  if arr[nx][ny] == 1:
    return
  clean(nx, ny, d)

clean(r, c, dir)
print(cnt)