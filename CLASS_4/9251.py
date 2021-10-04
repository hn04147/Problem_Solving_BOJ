import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

def lcs(a, b):
  c = [[0] * (len(a) + 1) for _ in range(len(b) + 1)]
  for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
      if b[i - 1] == a[j - 1]:
        c[i][j] = c[i - 1][j - 1] + 1
      else:
        c[i][j] = max(c[i][j -1], c[i - 1][j])
  return c

print(lcs(a, b)[-1][-1])