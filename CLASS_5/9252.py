import sys
from pprint import pprint

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

def lcs(a, b):
  c = [[0] * (len(a) + 1) for _ in range(len(b) + 1)]
  d = [['' for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]

  for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
      if b[i - 1] == a[j - 1]:
        c[i][j] = c[i - 1][j - 1] + 1
        d[i][j] = "left-up"
      elif c[i - 1][j] >= c[i][j - 1]:
        c[i][j] = c[i - 1][j]
        d[i][j] = "up"
      else:
        c[i][j] = c[i][j - 1]
        d[i][j] = "left"
  return c, d

def print_lcs(a, b, d):
  len_a, len_b = len(a), len(b)
  arr = ''
  while d[len_b][len_a] != '':
    if d[len_b][len_a] == "up":
      len_b -= 1
    elif d[len_b][len_a] == "left":
      len_a -= 1
    elif d[len_b][len_a] == "left-up":
      arr += b[len_b - 1]
      len_b -= 1
      len_a -= 1

  return ''.join(reversed(arr))

lcs_, d_ = lcs(a, b)
print(lcs_[-1][-1])
print(print_lcs(a, b, d_))