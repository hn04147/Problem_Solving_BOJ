import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

def can_bishop(x, y, size):
  global arr

  dx = [-1, -1, 1, 1]
  dy = [-1, 1, 1, -1]
  for i in range(4):
    m, n = x + dx[i], y + dy[i]
    while 0 <= m < size and 0 <= n < size:
      # print(f'({m}, {n})')
      if arr[m][n] == 2:
        return False
      m, n = m + dx[i], n + dy[i]
  return True

def back(x, y):
  