import sys
input = sys.stdin.readline

arr = [list(map(int, input().rstrip())) for _ in range(9)]

def check_row(i, x, y):
  for j in range(9):
    if arr[x][j] == i:
      return False
  return True

def check_col(i, x, y):
  for j in range(9):
    if arr[j][y] == i:
      return False
  return True

def check_3x3(i, x, y):
  for m in range(x // 3 * 3, x // 3 * 3 + 3):
    for n in range(y // 3 * 3, y // 3 * 3 + 3):
      if arr[m][n] == i:
        return False
  return True

flag = False

def track(n):
  global flag
  x = n // 9
  y = n % 9

  if flag:
    return

  if n == 81:
    flag = True
    for i in range(9):
      for j in range(9):
        print(arr[i][j], end = '')
      print()
    return

  if arr[x][y] != 0:
    track(n + 1)
  else:
    for i in range(1, 10):
      if check_row(i, x, y) and check_col(i, x, y) and check_3x3(i, x, y):
        arr[x][y] = i
        track(n + 1)
        arr[x][y] = 0

  return

track(0)