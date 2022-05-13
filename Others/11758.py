import sys
input = sys.stdin.readline

x1, y1 = map(int, input().rstrip().split())
x2, y2 = map(int, input().rstrip().split())
x3, y3 = map(int, input().rstrip().split())

def ccw(x1, y1, x2, y2, x3, y3):
  ans = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
  if ans < 0:
    return -1
  elif ans > 0:
    return 1
  else:
    return 0

print(ccw(x1, y1, x2, y2, x3, y3))