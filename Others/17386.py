import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().rstrip().split())
x3, y3, x4, y4 = map(int, input().rstrip().split())
A = [x1, y1]
B = [x2, y2]
C = [x3, y3]
D = [x4, y4]

def CCW(a, b, c):
  ans = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
  if ans < 0:
    return -1
  elif ans > 0:
    return 1
  else:
    return 0

CCW_ABC = CCW(A, B, C)
CCW_ABD = CCW(A, B, D)
CCW_CDA = CCW(C, D, A)
CCW_CDB = CCW(C, D, B)

if CCW_ABC * CCW_ABD < 0 and CCW_CDA * CCW_CDB < 0:
  print(1)
else:
  print(0)