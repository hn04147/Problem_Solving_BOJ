n, m = map(int, input().split())
if m > (n // 2):
  m = n - m

up, down = 1, 1
for i in range(n, n - m, -1):
  up *= i
for i in range(1, m + 1):
  down *= i
print(up // down)