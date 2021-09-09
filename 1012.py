'''
Case 1:
Input:
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

Output:
5
1

Case 2:
Input:
1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0

Output:
2
'''

import sys

def dfs(arr, x, y, n, m):
  arr[x][y] = 0
  if x >= 1 and arr[x-1][y] == 1:
    dfs(arr, x-1, y, n, m)
  if y < (m - 1) and arr[x][y+1] == 1:
    dfs(arr, x, y+1, n, m)
  if x < (n - 1) and arr[x+1][y] == 1:
    dfs(arr, x+1, y, n, m)
  if y >= 1 and arr[x][y-1] == 1:
    dfs(arr, x, y-1, n, m)
  return

t = int(input())
answer = []

for i in range(t):
  count = 0
  m, n, k = map(int, sys.stdin.readline().strip().split())
  arr = [[0] * m for _ in range(n)]
  for _ in range(k):
    x, y = map(int, sys.stdin.readline().strip().split())
    arr[y][x] = 1
  
  for i in range(n):
    for j in range(m):
      if arr[i][j] == 1:
        dfs(arr, i, j, n, m)
        count += 1

  answer.append(count)

for i in answer:
  print(i)