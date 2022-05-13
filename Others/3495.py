import sys
input = sys.stdin.readline

m, n = map(int, input().split())
pic = [list(input().rstrip()) for _ in range(m)]

area = 0

for i in range(m):
  in_pic = False
  for j in range(n):
    if pic[i][j] == '.':
      if in_pic:
        area += 1
    else:
      area += .5
      if not in_pic:
        in_pic = True
      else:
        in_pic = False

print(int(area))