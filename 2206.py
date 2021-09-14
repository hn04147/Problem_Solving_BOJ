'''
Example 1)
Input:
6 4
0100
1110
1000
0000
0111
0000

Output: 
15

Example 2)
Input:
4 4
0111
1111
1111
1110

Output:
-1
'''

from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for i in arr:
  idx = input()
  for j in idx:
    i.append(int(j))

count = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
queue = deque()

queue.append([0, 0, 0])          # 3번째 인자가 0이면 아직 벽을 부수지 않았음, 1이면 벽을 한 번 부숨
arr[0][0] = 2                    # 한 번 방문하였으면 2로 바꿈
answer_exist = False

while queue:
  count += 1
  for _ in range(len(queue)):
    item = queue.popleft()

    if item[0] == (n - 1) and item[1] == (m - 1):
      answer_exist = True
      break

    for i in range(4):
      next_pos = [item[0] + dx[i], item[1] + dy[i]]
      if 0 <= next_pos[0] < n and 0 <= next_pos[1] < m:
        if item[2] == 0:
          if arr[next_pos[0]][next_pos[1]] == 0:
            arr[next_pos[0]][next_pos[1]] = 2
            queue.append([next_pos[0], next_pos[1], 0])
          elif arr[next_pos[0]][next_pos[1]] == 1:
            arr[next_pos[0]][next_pos[1]] = 2
            queue.append([next_pos[0], next_pos[1], 1])
        else:
          if arr[next_pos[0]][next_pos[1]] == 0:
            arr[next_pos[0]][next_pos[1]] = 2
            queue.append([next_pos[0], next_pos[1], 1])

if answer_exist:
  print(count)
else:
  print(-1)