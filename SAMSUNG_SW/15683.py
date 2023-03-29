import sys
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
room = [list(map(int, input().rstrip().split())) for _ in range(n)]

CCTVs = []
for i in range(n):
    for j in range(m):
        if 1 <= room[i][j] <= 5:
            CCTVs.append((room[i][j], i, j))
CCTV_num = len(CCTVs)
CCTVs.append((-1, -1, -1))

dirs = [
    [],
    [[(0, 1)], [(-1, 0)], [(0, -1)], [(1, 0)]],
    [[(0, 1), (0, -1)], [(-1, 0), (1, 0)]],
    [[(0, 1), (-1, 0)], [(-1, 0), (0, -1)], [(0, -1), (1, 0)], [(1, 0), (0, 1)]],
    [[(0, 1), (-1, 0), (0, -1)], [(-1, 0), (0, -1), (1, 0)], [(0, -1), (1, 0), (0, 1)], [(1, 0), (0, 1), (-1, 0)]],
    [[(0, 1), (-1, 0), (0, -1), (1, 0)]]
]

def check_space(room, camera, dir_num):
    camera_type, x, y = camera
    directions = dirs[camera_type][dir_num]

    for dx, dy in directions:
        nx, ny = x, y

        while 0 <= nx + dx < n and 0 <= ny + dy < m:
            nx += dx
            ny += dy

            if room[nx][ny] == 6:
                break
            elif room[nx][ny] == 0:
                room[nx][ny] = -1

    return room

ans = n * m

def check(room, cnt):
    global ans

    if cnt == CCTV_num:
        tmp = sum([i.count(0) for i in room])
        if tmp < ans:
            ans = tmp
        return

    camera_type, x, y = CCTVs[cnt]
    dir_len = len(dirs[camera_type])

    for i in range(dir_len):
        room_ = check_space(deepcopy(room), [camera_type, x, y], i)
        check(room_, cnt+1)

check(room, 0)

print(ans)