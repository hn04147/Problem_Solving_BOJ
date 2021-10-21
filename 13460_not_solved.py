import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(m)]
red, blue, hole = [0, 0], [0, 0], [0, 0]
red_hole, blue_hole = False, False
cnt = 0
for i in range(m):
  for j in range(n):
    if arr[i][j] == 'R':
      red = [i, j]
    elif arr[i][j] == 'B':
      blue = [i, j]
    elif arr[i][j] == 'O':
      hole = [i, j]

def prt():
  for i in range(m):
    for j in range(n):
      print(arr[i][j], end = '')
    print()

q = deque()
q.append([red, blue])

