import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())

  points = set()
  arr = []
  ans = 0

  for _ in range(n):
    x, y = map(int, input().rstrip().split())
    points.add((x, y))
    arr.append((x, y))

  for i in range(n):
    for j in range(n):
      if i == j:
        continue
      
      x1, y1 = arr[i]
      x2, y2 = arr[j]
      x_diff = x1 - x2
      y_diff = y1 - y2

      if ans >= x_diff ** 2 + y_diff ** 2:
        continue

      x3, y3 = x2 - y_diff, y2 + x_diff
      x4, y4 = x1 - y_diff, y1 + x_diff

      if (x3, y3) in points and (x4, y4) in points:
        ans = max(ans, x_diff ** 2 + y_diff ** 2)
    
  print(ans)