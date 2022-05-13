import sys
input = sys.stdin.readline

m, n, x, y, k = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(m)]
numbers = list(map(int, input().rstrip().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]       #[front, up, back, down, left, right]
#                                     2           [2, 1, 5, 6, 4, 3]
#                                   4 1 3
#                                     5
#                                     6       

def move(num):
  front, up, back, down, left, right = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
  if num == 1:
    return [front, left, back, right, down, up]
  elif num == 2:
    return [front, right, back, left, up, down]
  elif num == 3:
    return [up, back, down, front, left, right]
  else:
    return [down, front, up, back, left, right]

for num in numbers:
  nx = x + dx[num]
  ny = y + dy[num]

  if 0 <= nx < m and 0 <= ny < n:
    x, y = nx, ny
    dice = move(num)
    if graph[x][y] == 0:
      graph[x][y] = dice[3]
    else:
      dice[3] = graph[x][y]
      graph[x][y] = 0
    
    print(dice[1])