import sys
from pprint import pprint
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
skills = [
    [[-2, 0, 0.02], [2, 0, 0.02], [-1, -1, 0.1], [1, -1, 0.1], [-1, 0, 0.07], [1, 0, 0.07], [-1, 1, 0.01], [1, 1, 0.01], [0, -2, 0.05], [0, -1, 0]],
    [[-1, -1, 0.01], [-1, 1, 0.01], [0, -2, 0.02], [0, 2, 0.02], [0, -1, 0.07], [0, 1, 0.07], [1, -1, 0.1], [1, 1, 0.1], [2, 0, 0.05], [1, 0, 0]],
    [[2, 0, 0.02], [-2, 0, 0.02], [1, 1, 0.1], [-1, 1, 0.1], [1, 0, 0.07], [-1, 0, 0.07], [1, -1, 0.01], [-1, -1, 0.01], [0, 2, 0.05], [0, 1, 0]],
    [[1, 1, 0.01], [1, -1, 0.01], [0, 2, 0.02], [0, -2, 0.02], [0, 1, 0.07], [0, -1, 0.07], [-1, 1, 0.1], [-1, -1, 0.1], [-2, 0, 0.05], [-1, 0, 0]]
]

direction = 0
x, y = N // 2, N // 2
step = 1

ans = 0

while True:
    if x == 0 and y == 0:
        break
    
    for _ in range(2):
        for i in range(step):
            if x == 0 and y == 0:
                break
            x, y = x + dx[direction], y + dy[direction]

            sand = 0
            skill = skills[direction]
            for j in range(9):
                nx = x + skill[j][0]
                ny = y + skill[j][1]
                weight = skill[j][2]
                sand_weight = (graph[x][y] * weight) // 1

                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += sand_weight
                else:
                    ans += sand_weight

                sand += sand_weight

            nx = x + skill[9][0]
            ny = y + skill[9][1]
            sand_weight = graph[x][y] - sand

            if 0 <= nx < N and 0 <= ny < N:
                graph[nx][ny] += sand_weight
            else:
                ans += sand_weight

            graph[x][y] = 0
        
        direction = (direction + 1) % 4
    step += 1

print(int(ans))