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
one_point = True

if ccw_1 == 0 and ccw_2 == 0:
  if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <= max(y3, y4) and max(y1, y2) >= min(y3, y4):
    ans = 1
elif ccw_1 <= 0 and ccw_2 <= 0:
  ans = 1

print(ans)

if ans == 1:
  if x1 == x2:
    if x3 == x4:
      x = x1
      if min(y1, y2) == max(y3, y4) and max(y1, y2) > min(y3, y4):
        y = y1
      elif min(y3, y4) == max(y1, y2) and max(y3, y4) > min(y1, y2):
        y = y3
      print(x, y)
    else:
      x = x1
      y = ((y4 - y3) / (x4 - x3)) * (x1 - x4) + y4
      print(x, y)
  elif x3 == x4:
    x = x3
    y = ((y2 - y1) / (x2 - x1)) * (x3 - x2) + y2
    print(x, y)
  else:
    a1 = (y2 - y1) / (x2 - x1)
    b1 = y1 - x1 * a1
    a2 = (y4 - y3) / (x4 - x3)
    b2 = y3 - x3 * a2

    if a1 == a2 and b1 == b2:
      if max(x1, x2) == min(x3, x4) and max(y1, y2) == min(y3, y4) and min(x1, x2) < max(x3, x4) and min(y1, y2) < max(y3, y4): 
        x = max(x1, x2)
        y = max(y1, y2)
      elif max(x3, x4) == min(x1, x2) and max(y3, y4) == min(y1, y2) and min(x3, x4) < max(x1, x2) and min(y3, y4) < max(y1, y2):
        x = max(x3, x4)
        y = max(y3, y4)
      else:
        one_point = False
    else:
      x = (b2 - b1) / (a1 - a2)
      y = a1 * x + b1

    if one_point:
      print(x, y)