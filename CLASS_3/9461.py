import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
  n = int(input().strip())
  p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
  if n < 11:
    print(p[n])
  else:
    for i in range(11, n + 1):
      p.append(p[i-1] + p[i - 5])
    print(p[n])