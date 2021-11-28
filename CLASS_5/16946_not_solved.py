import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip())) for _ in range(m)]
space = [[[0, 0] for _ in range(n)] for _ in range(m)]
ans = [[0 for _ in range(n)] for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(m):
  for j in range(n):
    if arr[i][j] == 1 and visited[i][j] == 0:
      visited[i][j] = 1
      s = deque()



# for i in range(m):
#   for j in range(n):
#     if arr[i][j] == 1:
#       cnt = 1
#       idx_arr = [[i, j]]
#       q = deque()
#       arr[i][j] = -1
#       q.append([i, j])

#       while q:
#         x, y = q.popleft()
#         for k in range(4):
#           nx = x + dx[k]
#           ny = y + dy[k]

#           if 0 <= nx < m and 0 <= ny < n:
#             if arr[nx][ny] == 0:
#               arr[nx][ny] = -1
#               q.append([nx, ny])
#               idx_arr.append([nx, ny])
#               cnt += 1

#       for k in range(len(idx_arr)):
#         if k == 0:
#           arr[idx_arr[k][0]][idx_arr[k][1]] = 1
#         else:
#           arr[idx_arr[k][0]][idx_arr[k][1]] = 0
        
#       ans[i][j] = cnt

# for nums in ans:
#   for num in nums:
#     print(num, end = '')
#   print()