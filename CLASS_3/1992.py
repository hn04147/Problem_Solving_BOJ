import sys
input = sys.stdin.readline

n = int(input())
arr = ['']
for _ in range(n):
  arr.append(' ' + input().strip())

def check_same(x, y, width):
  num = arr[x][y]
  for i in range(x, x + width):
    for j in range(y, y + width):
      if arr[i][j] != num:
        return False
  return True

def press(x, y, width):
  if check_same(x, y, width):
    print(arr[x][y], end = '')
  else:
    print('(', end = '')
    press(x, y, width // 2)
    press(x, y + width // 2, width // 2)
    press(x + width // 2, y, width // 2)
    press(x + width // 2, y + width // 2, width // 2)
    print(')', end = '')

press(1, 1, n)