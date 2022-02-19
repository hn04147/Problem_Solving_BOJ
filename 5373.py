import sys
input = sys.stdin.readline

up = [['w' for _ in range(3)] for _ in range(3)]
down = [['y' for _ in range(3)] for _ in range(3)]
front = [['r' for _ in range(3)] for _ in range(3)]
back = [['o' for _ in range(3)] for _ in range(3)]
left = [['g' for _ in range(3)] for _ in range(3)]
right = [['b' for _ in range(3)] for _ in range(3)]

def print_cube():
  print('up:', *up, sep='\n')
  print('down: ', *down, sep='\n')
  print('front: ', *front, sep='\n')
  print('back: ', *back, sep='\n')
  print('left: ', *left, sep='\n')
  print('right: ', *right, sep='\n')

def rotate_clockwise(arr):
  result = [[arr[2][0], arr[1][0], arr[0][0]],
            [arr[2][1], arr[1][1], arr[0][1]],
            [arr[2][2], arr[1][2], arr[0][2]]]
  return result

def rotate_counterclockwise(arr):
  result = [[arr[0][2], arr[1][2], arr[2][2]],
            [arr[0][1], arr[1][1], arr[2][1]],
            [arr[0][0], arr[1][0], arr[2][0]]]
  return result

def rotate(method):
  global up, down, front, back, left, right
  s, d = method[0], method[1]
  
  if s == 'U':
    if d == '+':
      up = rotate_clockwise(up)
      idx = front[0]
      front[0] = right[0]
      right[0] = back[0]
      back[0] = left[0]
      left[0] = idx
    else:
      up = rotate_counterclockwise(up)
      idx = front[0]
      front[0] = left[0]
      left[0] = back[0]
      back[0] = right[0]
      right[0] = idx

  elif s == 'D':
    if d == '+':
      down = rotate_clockwise(down)
      idx = front[2]
      front[2] = left[2]
      left[2] = back[2]
      back[2] = right[2]
      right[2] = idx
    else:
      down = rotate_counterclockwise(down)
      idx = front[2]
      front[2] = right[2]
      right[2] = back[2]
      back[2] = left[2]
      left[2] = idx

  elif s == 'F':
    if d == '+':
      front = rotate_clockwise(front)
      idx = up[2]
      up[2] = [left[2][2], left[1][2], left[0][2]]
      left[2][2], left[1][2], left[0][2] = down[0][2], down[0][1], down[0][0]
      down[0] = [right[2][0], right[1][0], right[0][0]]
      right[2][0], right[1][0], right[0][0] = idx[2], idx[1], idx[0]
    else:
      front = rotate_counterclockwise(front)
      idx = up[2]
      up[2] = [right[0][0], right[1][0], right[2][0]]
      right[0][0], right[1][0], right[2][0] = down[0][2], down[0][1], down[0][0]
      down[0] = [left[0][2], left[1][2], left[2][2]]
      left[0][2], left[1][2], left[2][2] = idx[2], idx[1], idx[0]

  elif s == 'B':
    if d == '+':
      back = rotate_clockwise(back)
      idx = up[0]
      up[0] = [right[0][2], right[1][2], right[2][2]]
      right[0][2], right[1][2], right[2][2] = down[2][2], down[2][1], down[2][0]
      down[2] = [left[0][0], left[1][0], left[2][0]]
      left[0][0], left[1][0], left[2][0] = idx[2], idx[1], idx[0]
    else:
      back = rotate_counterclockwise(back)
      idx = up[0]
      up[0] = [left[2][0], left[1][0], left[0][0]]
      left[2][0], left[1][0], left[0][0] = down[2][2], down[2][1], down[2][0]
      down[2] = [right[2][2], right[1][2], right[0][2]]
      right[2][2], right[1][2], right[0][2] = idx[2], idx[1], idx[0]

  elif s == 'L':
    if d == '+':
      left = rotate_clockwise(left)
      idx = [up[0][0], up[1][0], up[2][0]]
      up[0][0], up[1][0], up[2][0] = back[2][2], back[1][2], back[0][2]
      back[2][2], back[1][2], back[0][2] = down[0][0], down[1][0], down[2][0]
      down[0][0], down[1][0], down[2][0] = front[0][0], front[1][0], front[2][0]
      front[0][0], front[1][0], front[2][0] = idx[0], idx[1], idx[2]
    else:
      left = rotate_counterclockwise(left)
      idx = [up[0][0], up[1][0], up[2][0]]
      up[0][0], up[1][0], up[2][0] = front[0][0], front[1][0], front[2][0]
      front[0][0], front[1][0], front[2][0] = down[0][0], down[1][0], down[2][0]
      down[0][0], down[1][0], down[2][0] = back[2][2], back[1][2], back[0][2]
      back[2][2], back[1][2], back[0][2] = idx[0], idx[1], idx[2]

  else:
    if d == '+':
      right = rotate_clockwise(right)
      idx = [up[0][2], up[1][2], up[2][2]]
      up[0][2], up[1][2], up[2][2] = front[0][2], front[1][2], front[2][2]
      front[0][2], front[1][2], front[2][2] = down[0][2], down[1][2], down[2][2]
      down[0][2], down[1][2], down[2][2] = back[2][0], back[1][0], back[0][0]
      back[2][0], back[1][0], back[0][0] = idx[0], idx[1], idx[2]
    else:
      right = rotate_counterclockwise(right)
      idx = [up[0][2], up[1][2], up[2][2]]
      up[0][2], up[1][2], up[2][2] = back[2][0], back[1][0], back[0][0]
      back[2][0], back[1][0], back[0][0] = down[0][2], down[1][2], down[2][2]
      down[0][2], down[1][2], down[2][2] = front[0][2], front[1][2], front[2][2]
      front[0][2], front[1][2], front[2][2] = idx[0], idx[1], idx[2]

n = int(input())

for _ in range(n):
  m = int(input())
  arr = list(input().rstrip().split())
  up = [['w' for _ in range(3)] for _ in range(3)]
  down = [['y' for _ in range(3)] for _ in range(3)]
  front = [['r' for _ in range(3)] for _ in range(3)]
  back = [['o' for _ in range(3)] for _ in range(3)]
  left = [['g' for _ in range(3)] for _ in range(3)]
  right = [['b' for _ in range(3)] for _ in range(3)]

  for a in arr:
    rotate(a)
  
  for i in up:
    for j in i:
      print(j, end='')
    print()