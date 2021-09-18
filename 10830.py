import sys

def matrix_mul(a, b):
  n = len(a)
  result = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      for m in range(n):
        result[i][j] += a[i][m] * b[m][j]
      result[i][j] %= 1000
  return result
  
def prod(matrix, b):
  if b == 1:
    return matrix
  elif b == 2:
    return matrix_mul(matrix, matrix)
  else:
    tmp = prod(matrix, b // 2)
    if b % 2 == 0:
      return matrix_mul(tmp, tmp)
    else:
      return matrix_mul(matrix_mul(tmp, tmp), matrix)


n, b = map(int, input().split())
mat = []
for _ in range(n):
  idx = list(map(int, sys.stdin.readline().split()))
  mat.append(idx)

result = prod(mat, b)

for i in range(n):
  for j in range(n):
    print('{} '.format(result[i][j] % 1000), end = '\n' if j == (n - 1) else '')