import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
time = 0
baby = [2, 0]
baby_loc = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            baby_loc = [i, j]

while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque([])
    q.append([baby_loc[0], baby_loc[1], 0])
    finish = False
    candidates = []

    while q:
        x, y, dist = q.popleft()
        for x_, y_ in zip(dx, dy):
            nx = x + x_
            ny = y + y_
            if 0 <= nx < n and 0 <= ny < n:
                if not finish:
                    if graph[nx][ny] == 0 or graph[nx][ny] == baby[0]:
                        if visited[nx][ny] == False:
                            visited[nx][ny] = True
                            q.append([nx, ny, dist+1])
                    elif graph[nx][ny] < baby[0] and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        finish = True
                        distance = dist + 1
                        candidates.append([distance, nx, ny])
                else:
                    if 0 < graph[nx][ny] < baby[0] and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        distance = dist + 1
                        candidates.append([distance, nx, ny])
    
    if len(candidates) == 0:
        break

    candidates = sorted(candidates, key = lambda x : (x[0], x[1], x[2]))
    distance, nx, ny = candidates[0][0], candidates[0][1], candidates[0][2]
    time += distance
    graph[nx][ny] = 9
    graph[baby_loc[0]][baby_loc[1]] = 0
    baby_loc = [nx, ny]
    baby[1] += 1
    if baby[0] == baby[1]:
        baby[0] += 1
        baby[1] = 0

print(time)