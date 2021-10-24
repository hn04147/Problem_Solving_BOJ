import sys
input = sys.stdin.readline

arr = [list(map(int, input().rstrip())) for _ in range(9)]

def track(x, y):
  if x == 9 and y == 0:
    return
  if arr[x][y] == 0:
    col_arr = []
    rec_arr = []
    for i in range(9):
      col_arr.append(arr[x][i])
    for nx in range(x // 3 * 3, x // 3 * 3 + 1):
      for ny in range(y // 3 * 3, y // 3 * 3 + 1):
        rec_arr.append(arr[nx][ny])
    for i in range(1, 10):
      if i not in arr[x] and i not in col_arr and i not in rec_arr:
        arr[x][y] = i
        if y == 8:
          track(x + 1, 0)
        else:
          track(x, y + 1)
        arr[x][y] = 0
  
  if y == 8:
    track(x + 1, 0)
  else:
    track(x, y + 1)
  return

track(0, 0)
print(arr)