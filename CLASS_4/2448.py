n = int(input())
arr = [[' '] * (n * 2) for _ in range(n + 1)]

def print_star(arr):
  for i in range(1, len(arr)):
    for j in range(1, len(arr[0])):
      print(arr[i][j], end = '')
    print()

x1, y1 = 1, 1
x2, y2 = n, n * 2

def add_star(x1, y1, x2, y2):
  height = x2 - x1 + 1
  width = y2 - y1 + 1
  if height > 3:
    new_height = height // 2
    new_width = width // 2
    add_star(x1, y1 + (width - new_width) // 2, x1 + new_height - 1, y2 - (width - new_width) // 2)     # up
    add_star(x1 + new_height, y1, x2, y1 + new_width - 1)                                               # left down
    add_star(x1 + new_height, y1 + new_width + 1, x2, y2)                                               # right down
  elif height == 3:
    arr[x1][y1 + 2] = '*'
    arr[x1 + 1][y1 + 1] = '*'
    arr[x1 + 1][y1 + 3] = '*'
    for i in range(5):
      arr[x2][y1 + i] = '*'

add_star(1, 1, n, n * 2 - 1)
print_star(arr)