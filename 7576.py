'''
Example 1)
Input:
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

Output:
8

Example 2)
Input:
6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

Output:
-1

Example 3)
Input:
6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1

Output:
6

Example 4)
input:
5 5
-1 1 0 0 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 0 0 0 0

Output: 
14

Example 5)
Input:
2 2
1 -1
-1 1

Output:
0
'''

n, m = list(map(int, input().split()))
arr = []
for _ in range(m):
  arr.append(list(map(int, input().split())))

def find_onion(arr, m, n):
  queue = []
  count = -1
  for i in range(m):
    for j in range(n):
      if arr[i][j] == 1:
        queue.append([i, j])
  while queue:
    count += 1
    for i in range(len(queue)):
      x, y = queue.pop(0)
      if x > 0:
        if arr[x-1][y] == 0:
          arr[x-1][y] = 1
          queue.append([x-1, y])
      if y > 0:
        if arr[x][y-1] == 0:
          arr[x][y-1] = 1
          queue.append([x, y-1])
      if x < (m-1):
        if arr[x+1][y] == 0:
          arr[x+1][y] = 1
          queue.append([x+1, y])
      if y < (n-1):
        if arr[x][y+1] == 0:
          arr[x][y+1] = 1
          queue.append([x, y+1])
  
  for i in arr:
    if 0 in i:
      return -1

  return count

def find_min_period(arr, m, n):
  for i in arr:
    if 0 in i:
      return(find_onion(arr, m, n))
  return 0

print(find_min_period(arr, m, n))