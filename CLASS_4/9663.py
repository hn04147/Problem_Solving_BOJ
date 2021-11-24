t = int(input())

board = [[0 for _ in range(t)] for _ in range(t)]
visited = [0 for _ in range(t)]
cnt = 0

def check_available(x, y):
  dx = [-1, 1, 1, -1]
  dy = [-1, -1, 1, 1]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    while nx >= 0 and ny >= 0 and nx < t and ny < t:
      if board[nx][ny] == 1:
        return False
      nx += dx[i]
      ny += dy[i]
  return True

def track(n):
  global board, cnt, visited

  if n == t:
    cnt += 1
    return
  else:
    for i in range(t):
      if visited[i] == 0:
        if check_available(n, i):
          visited[i] = 1
          board[n][i] = 1
          track(n + 1)
          board[n][i] = 0
          visited[i] = 0
  return

track(0)
print(cnt)