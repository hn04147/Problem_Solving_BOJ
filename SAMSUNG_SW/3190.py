import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())
apples = [list(map(int, input().rstrip().split())) for _ in range(k)]
l = int(input().rstrip())
changes = defaultdict(int)
for _ in range(l):
  x, c = input().rstrip().split()
  changes[int(x)] = c

dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
current_dir = 3
cnt = 0
snake = deque([[0, 0]])

while True:
  head = snake[-1]

  if cnt in changes:
    next_direction = changes[cnt]
    if next_direction == 'L':
      current_dir = (current_dir + 1) % 4
    else:
      current_dir = (current_dir - 1) % 4
  
  cnt += 1
  next_head = [head[0] + dir[current_dir][0], head[1] + dir[current_dir][1]]

  if 0 <= next_head[0] < n and 0 <= next_head[1] < n:
    if next_head in apples:
      if next_head in snake:
        break
      else:
        snake.append(next_head)
      apples.remove(next_head)
    else:
      snake.popleft()
      if next_head in snake:
        break
      else:
        snake.append(next_head)
    
    # if next_head in snake:
    #   break
    # else:
    #   if [next_head[0] + 1, next_head[1] + 1] in apples:
    #     snake.append(next_head)
    #     apples.remove([next_head[0] + 1, next_head[1] + 1])
    #   else:
    #     snake.append(next_head)
    #     snake.popleft()
  else:
    break

print(cnt)

'''
8
3
5 4
5 8
2 5
6
7 D
11 D
15 D
18 D
19 D
20 D
:::::::21

8
5
6 1
7 3
3 5
5 7
5 6
12
2 D
8 D
10 D
12 D
18 L
20 L
22 L
24 L
25 L
28 L
32 D
33 L
::::::::27
'''