import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

M, S = map(int, input().rstrip().split())
graph = [[deque([]) for _ in range(4)] for _ in range(4)]
for _ in range(M):
    fx, fy, d = map(int, input().rstrip().split())
    graph[fx-1][fy-1].append(d-1)
sx, sy = map(int, input().rstrip().split())
shark = [sx - 1, sy - 1]
smells = [[[False, 0] for _ in range(4)] for _ in range(4)]

# 물고기 움직이는 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 상어 움직이는 방향
dsx = [-1, 0, 1, 0]
dsy = [0, -1, 0, 1]

for _ in range(S):
    # 물고기 복제
    graph_copied = [[deque([]) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(len(graph[i][j])):
                graph_copied[i][j].append(graph[i][j][k])
    # print('처음')
    # pprint(graph)


    # 물고기 이동
    fish_moved = [[deque([]) for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            if graph[x][y]:
                while graph[x][y]:
                    ori_direction = graph[x][y].popleft()
                    idx = 0
                    while idx < 8:
                        nx = x + dx[ori_direction]
                        ny = y + dy[ori_direction]
                        if 0 <= nx < 4 and 0 <= ny < 4 and [nx, ny] != shark and smells[nx][ny][0] == False:
                            fish_moved[nx][ny].append(ori_direction)
                            break
                        else:
                            ori_direction = (ori_direction - 1) % 8
                            idx += 1
    for x in range(4):
        for y in range(4):
            if fish_moved[x][y]:
                while fish_moved[x][y]:
                    fish = fish_moved[x][y].popleft()
                    graph[x][y].append(fish)
    # print('물고기 이동 후')
    # pprint(graph)


    # 상어 이동
    max_fish = 0
    max_sequence = []
    min_sequence = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                count = 0
                nx1, ny1 = shark[0] + dsx[i], shark[1] + dsy[i]
                nx2, ny2 = nx1 + dsx[j], ny1 + dsy[j]
                nx3, ny3 = nx2 + dsx[k], ny2 + dsy[k]
                if 0 <= nx1 < 4 and 0 <= ny1 < 4 and 0 <= nx2 < 4 and 0 <= ny2 < 4 and 0 <= nx3 < 4 and 0 <= ny3 < 4:
                    if len(min_sequence) == 0:
                        min_sequence = [[nx1, ny1], [nx2, ny2], [nx3, ny3]]
                    sequence = [[nx1, ny1], [nx2, ny2], [nx3, ny3]]
                    sequence_set = set(list(map(tuple, sequence)))
                    for s in sequence_set:
                        count += len(graph[s[0]][s[1]])
                    if count > max_fish:
                        max_fish = count
                        max_sequence = sequence


    # 상어 이동 경로에 있는 물고기 제거 및 냄새 추가
    for sequence in max_sequence:
        x, y = sequence[0], sequence[1]
        if graph[x][y]:
            graph[x][y] = deque([])
            smells[x][y] = [True, 2]
    if len(max_sequence) == 0:
        shark = min_sequence[2]
    else:
        shark = max_sequence[2]
    # print('물고기 제거, 냄새 추가 후')
    # pprint(graph)


    # 두 번 전 생긴 물고기 냄새 제거
    for x in range(4):
        for y in range(4):
            if smells[x][y][0] == True:
                if smells[x][y][1] > 0:
                    smells[x][y][1] = smells[x][y][1] - 1
                elif smells[x][y][1] == 0:
                    smells[x][y] = [False, 0]


    # 복제한 물고기 추가
    for x in range(4):
        for y in range(4):
            if graph_copied[x][y]:
                while graph_copied[x][y]:
                    fish = graph_copied[x][y].popleft()
                    graph[x][y].append(fish)
    # print('물고기 복제 후')
    # pprint(graph)
    # print('상어 위치', shark)
    # print('냄새')
    # pprint(smells)


ans = 0
for x in range(4):
    for y in range(4):
        ans += len(graph[x][y])

print(ans)