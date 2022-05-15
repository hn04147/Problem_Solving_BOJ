'''
Example 1)
Input:
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1

Output:
-1

Example 2)
Input:
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0

Output:
4

Example 3)
Input:
4 3 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-1 -1 -1 -1
1 1 1 -1

Output:
0
'''

from collections import deque

def find_onion(arr, m, n, h):
  dx = [-1, 0, 1, 0, 0, 0]
  dy = [0, 1, 0, -1, 0, 0]
  dz = [0, 0, 0, 0, 1, -1]

  for i in range(h):
    for j in arr[i]:
      if 0 not in j:
        return 0

  queue = deque()
  count = -1
  
  for i in range(h):
    for j in range(m):
      for k in range(n):
        if arr[i][j][k] == 1:
          queue.append([i, j, k])
  
  while queue:
    count += 1
    for _ in range(len(queue)):
      pos_z, pos_x, pos_y = queue.popleft()
      arr[pos_z][pos_x][pos_y] = 1
      for idx in range(6):
        if 0 <= (pos_z + dz[idx]) < h:
          if 0 <= (pos_x + dx[idx]) < m:
            if 0 <= (pos_y + dy[idx]) < n:
              if arr[pos_z + dz[idx]][pos_x + dx[idx]][pos_y + dy[idx]] == 0:
                queue.append([pos_z + dz[idx], pos_x + dx[idx], pos_y + dy[idx]])

  for i in range(h):
    for j in arr[i]:
      if 0 in j:
        return -1

  return count

if __name__ == '__main__':
  n, m, h = list(map(int, input().split()))
  arr = []
  for z in range(h):
    floor = []
    for _ in range(m):
      floor.append(list(map(int, input().split())))
    arr.append(floor)

  print(find_onion(arr, m, n, h))