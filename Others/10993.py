n = int(input())

star = [[' ' for _ in range(2 ** (n + 1) - 3)] for _ in range(2 ** n - 1)]

def print_star(num, coor, width, height):
  x = coor[0]
  y = coor[1]

  if num % 2 == 0:
    for i in range(y, y + width):
      star[x][i] = '*'
    star[x + height - 1][y + width // 2] = '*'

    idx = 1
    for i in range(x + 1, x + height - 1):
      star[i][y + idx] = '*'
      star[i][y + width - 1 - idx] = '*'
      idx += 1

  else:
    for i in range(y, y + width):
      star[x + height - 1][i] = '*'
    star[x][y + width // 2] = '*'

    idx = 1
    for i in range(x + height - 2, x, -1):
      star[i][y + idx] = '*'
      star[i][y + width - 1 - idx] = '*'
      idx += 1

x, y = 0, 0

for num in range(n, 0, -1):
  width = 2 ** (num + 1) - 3
  height = 2 ** num - 1
  print_star(num, [x, y], width, height)

  if num % 2 == 0:
    x += 1
  else:
    x = x + height // 2
  y = y + width // 4 + 1

for points in star:
  for point in points:
    print(point, end = '')
  print('\n', end = '')