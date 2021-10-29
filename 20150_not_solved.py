import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

def ccw(x1, y1, x2, y2, x3, y3):
  ans = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
  if ans < 0:
    return -1
  elif ans > 0:
    return 1
  else:
    return 0

def judge():
  for i in range(n - 1):
    for j in range(i + 1, n):
      ccwabc = ccw(arr[0][0], arr[0][1], arr[0][2], arr[0][3], arr[1][0], arr[1][1])
      ccwabd = ccw(arr[0][0], arr[0][1], arr[0][2], arr[0][3], arr[1][2], arr[1][3])
      ccwcda = ccw(arr[1][0], arr[1][1], arr[1][2], arr[1][3], arr[0][0], arr[0][1])
      ccwcdb = ccw(arr[1][0], arr[1][1], arr[1][2], arr[1][3], arr[0][2], arr[0][3])

      if ccwabc * ccwabd == 0 and ccwcda * ccwcdb == 0:
        if min(arr[0][0], arr[0][2]) <= max(arr[1][0], arr[1][2]) and max(arr[0][0], arr[0][2]) >= min(arr[1][0], arr[1][2]):
          if min(arr[0][1], arr[0][3]) <= max(arr[1][1], arr[1][3]) and max(arr[0][1], arr[0][3]) >= min(arr[1][1], arr[1][3]):
            return 1
      elif ccwabc * ccwabd <= 0 and ccwcda * ccwcdb <= 0:
        return 1
  
  return 0

print(judge())