import sys
from pprint import pprint
input = lambda: sys.stdin.readline().rstrip()

R, C, M = map(int, input().split())
grid = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    grid[r-1][c-1] = [z, s, d-1]

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
ans = 0

def change_direction(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2

for j in range(C):
    if M == 0:
        break

    for i in range(R):
        if grid[i][j]:
            ans += grid[i][j][0]
            grid[i][j] = []
            M -= 1
            break

    next_grid = [[[] for _ in range(C)] for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if grid[x][y]:
                nx, ny = x, y
                size, speed, direction = grid[x][y]
                for _ in range(speed):
                    if 0 <= nx + dirs[direction][0] < R and 0 <= ny + dirs[direction][1] < C:
                        nx += dirs[direction][0]
                        ny += dirs[direction][1]
                    else:
                        direction = change_direction(direction)
                        nx = nx + dirs[direction][0]
                        ny = ny + dirs[direction][1]
                if next_grid[nx][ny]:
                    if size > next_grid[nx][ny][0]:
                        next_grid[nx][ny] = [size, speed, direction]
                    M -= 1
                else:
                    next_grid[nx][ny] = [size, speed, direction]

    grid = [[[] for _ in range(C)] for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if next_grid[x][y]:
                grid[x][y] = next_grid[x][y]

print(ans)