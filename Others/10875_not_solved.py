# 시간 초과 코드

l = int(input())
n = int(input())
steps = {}

index = 0
for _ in range(n):
  i, t = input().split()
  index += int(i)
  steps[str(index)] = t

time = 0
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
direction = 1

#graph = [[0 for _ in range(2*l+1)] for _ in range(2*l+1)]
#graph[l][l] = 1
snakes = [[l, l]]
print(snakes)
pos = [l, l]

def get_direction(direction_):
  if direction_ == 'L':
    return direction - 1 if direction > 0 else 3
  elif direction_ == 'R':
    return direction + 1 if direction < 3 else 0

def check_gameover(next_pos):
  global graph

  if next_pos[0] < 0 or next_pos[0] > 2*l or next_pos[1] < 0 or next_pos[1] > 2*l:
    return True
  #if graph[next_pos[0]][next_pos[1]] == 1:
  if [next_pos[0], next_pos[1]] in snakes:
    return True

while True:
  if str(time) in steps:
    direction = get_direction(steps[str(time)])
  pos = [pos[0] + directions[direction][0], pos[1] + directions[direction][1]]

  if check_gameover(pos):
    break

  time += 1
  #graph[pos[0]][pos[1]] = 1
  snakes.append([pos[0], pos[1]])

print(snakes)

print(time+1)