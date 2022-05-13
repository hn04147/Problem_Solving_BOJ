'''
Example 1)
Input: 
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1

Output:
5
28
0
'''

from collections import deque

dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

time = int(input())
for _ in range(time):
  count = 0
  length = int(input())
  arr = [[0] * length for _ in range(length)]
  start_x, start_y = map(int, input().split())
  end_x, end_y = map(int, input().split())

  status = True

  if start_x == end_x and start_y == end_y:
    status = False
    count = 0
  else:
    queue = deque()
    queue.append([start_x, start_y])

    while status:
      count += 1
      for _ in range(len(queue)):
        current_pos = queue.popleft()
        for i in range(8):
          next_pos = [current_pos[0] + dx[i], current_pos[1] + dy[i]]
          if next_pos[0] == end_x and next_pos[1] == end_y:
            status = False
            break
          if 0 <= next_pos[0] < length and 0 <= next_pos[1] < length:
            if arr[next_pos[0]][next_pos[1]] == 0:
              queue.append([next_pos[0], next_pos[1]])
              arr[next_pos[0]][next_pos[1]] = 1

  print(count)