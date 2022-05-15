import sys
input = sys.stdin.readline

n = int(input())
arr = [[0 for _ in range(n + 1)]]
for _ in range(n):
  arr.append([0] + list(map(int, input().strip().split())))

def check_color(x1, y1, x2, y2):
  color = arr[x1][y1]
  idx = 0
  is_break = False
  for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
      idx += 1
      if arr[i][j] != color:
        color = -1
        is_break = True
        break
    if is_break:
      break
  return color

white, blue = 0, 0

def recursive(x1, y1, x2, y2):
  global white, blue
  length = x2 - x1 + 1

  result = check_color(x1, y1, x2, y2)
  if result != -1:
    if result == 0:
      white += 1
    else:
      blue += 1
  else:
    for i in range(x1, x2 + 1, length // 2):
      for j in range(y1, y2 + 1, length // 2):
        recursive(i, j, i + length // 2 - 1, j + length // 2 - 1)

recursive(1, 1, n, n)
print(white)
print(blue)