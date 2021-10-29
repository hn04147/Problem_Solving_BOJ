import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().rstrip().split())
x3, y3, x4, y4 = map(int, input().rstrip().split())

def ccw(x1, y1, x2, y2, x3, y3):
  ans = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
  if ans < 0:
    return -1
  elif ans > 0:
    return 1
  else:
    return 0

ccw_1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
ccw_2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

ans = 0

if ccw_1 == 0 and ccw_2 == 0:
  if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <= max(y3, y4) and max(y1, y2) >= min(y3, y4):
    ans = 1
elif ccw_1 <= 0 and ccw_2 <= 0:
  ans = 1

print(ans)