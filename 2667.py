'''
Input:
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

Output:
3
7
8
9
'''
import sys

n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int, sys.stdin.readline().strip())))

def dfs(arr, x, y):
  global count
  arr[x][y] = 0
  count += 1
  if x >= 1 and arr[x-1][y] == 1:
    dfs(arr, x-1, y)
  if y < (n - 1) and arr[x][y+1] == 1:
    dfs(arr, x, y+1)
  if x < (n - 1) and arr[x+1][y] == 1:
    dfs(arr, x+1, y)
  if y >= 1 and arr[x][y-1] == 1:
    dfs(arr, x, y-1)
  
result = []

for i in range(n):
  for j in range(n):
    if arr[i][j] == 1:
      count = 0
      dfs(arr, i, j)
      result.append(count)

result.sort()

print(len(result))
for i in result:
  print(i)