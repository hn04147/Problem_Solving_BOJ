import sys
input = sys.stdin.readline

n = int(input())

# for _ in range(n):
#   m, n, x, y = map(int, input().rstrip().split())
#   flag = False
#   nx, ny = 0, 0
#   ans = 0
#   for i in range(m * n):
#     if nx == x and ny == y:
#       flag = True
#       ans = i
#       break
#     else:
#       nx = nx + 1 if nx < m else 1
#       ny = ny + 1 if ny < n else 1
    
#   if flag:
#     print(ans)
#   else:
#     print(-1)

for _ in range(n):
  m, n, x, y = map(int, input().rstrip().split())
  flag = True
  while x <= m * n:
    if x % n == y % n:
      print(x)
      flag = False
      break
    x += m
  if flag:
    print(-1)