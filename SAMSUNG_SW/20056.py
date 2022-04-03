import sys
import math
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())
balls = deque([list(map(int, input().rstrip().split())) for _ in range(M)])
for i in range(len(balls)):
    balls[i][0] -= 1
    balls[i][1] -= 1

graph = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(N)]   # [fireball의 개수, 질량의 합, 속력의 합, 방향의 합]
for ball in balls:
    r, c, m, s, d = ball
    graph[r][c][0] += 1
    graph[r][c][1] += m
    graph[r][c][2] += s
    graph[r][c][3] += d

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    graph = [[[0, 0, 0, []] for _ in range(N)] for _ in range(N)]

    for _ in range(len(balls)):
        x, y, m, s, d = balls.popleft()

        nx = (x + s * dx[d]) % N
        ny = (y + s * dy[d]) % N

        graph[nx][ny][0] += 1
        graph[nx][ny][1] += m
        graph[nx][ny][2] += s
        graph[nx][ny][3].append(d)

    for i in range(N):
        for j in range(N):
            if graph[i][j][0] == 1:
                balls.append([i, j, graph[i][j][1], graph[i][j][2], graph[i][j][3][0]])
            elif graph[i][j][0] > 1:
                m, s, d = graph[i][j][1], graph[i][j][2], graph[i][j][3]
                m = m // 5
                s = s // graph[i][j][0]

                even, odd = 0, 0
                for k in d:
                    if k in [0, 2, 4, 6]:
                        even += 1
                    else:
                        odd += 1
                if even == 0 or odd == 0:
                    directions = [0, 2, 4, 6]
                else:
                    directions = [1, 3, 5, 7]

                if m > 0:
                    for k in range(4):
                        balls.append([i, j, m, s, directions[k]])

if len(balls) == 0:
    print(0)
else:
    print(sum([i[2] for i in balls]))