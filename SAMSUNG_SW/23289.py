import sys
from pprint import pprint
from copy import deepcopy
input = lambda : sys.stdin.readline().rstrip()

r, c, k = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
fans = []
targets = []
temperatures = [[0 for _ in range(c)] for _ in range(r)]
w = int(input())
walls = [[{'U': False, 'R': False} for _ in range(c)] for _ in range(r)]
choco = 0

for i in range(r):
    for j in range(c):
        if 1 <= room[i][j] <= 4:
            fans.append((i, j, room[i][j]))
        elif room[i][j] == 5:
            targets.append((i, j))

for _ in range(w):
    x, y, t = map(int, input().split())
    if t == 0:
        walls[x-1][y-1]['U'] = True 
    else:
        walls[x-1][y-1]['R'] = True


def wind():
    result = [[0 for _ in range(c)] for _ in range(r)]

    for x, y, direction in fans:
        temp = [[-1 for _ in range(c)] for _ in range(r)]

        # RIGHT
        if direction == 1:
            temp[x][y+1] = 5
            for j in range(1, 5):
                if y + j + 1 >= c:
                    break
                ny = y + j
                for nx in range(x-j+1, x+j):
                    if 0 <= nx < r and temp[nx][ny] != -1:
                        if nx - 1 >= 0 and not walls[nx][ny]['U'] and not walls[nx-1][ny]['R']:
                            temp[nx-1][ny+1] = 5 - j
                        if not walls[nx][ny]['R']:
                            temp[nx][ny+1] = 5 - j
                        if nx + 1 < r and not walls[nx+1][ny]['U'] and not walls[nx+1][ny]['R']:
                            temp[nx+1][ny+1] = 5 - j

        # LEFT
        elif direction == 2:
            temp[x][y-1] = 5
            for j in range(1, 5):
                if y - j - 1 < 0:
                    break
                ny = y - j
                for nx in range(x-j+1, x+j):
                    if 0 <= nx < r and temp[nx][ny] != -1:
                        if nx - 1 >= 0 and not walls[nx][ny]['U'] and not walls[nx-1][ny-1]['R']:
                            temp[nx-1][ny-1] = 5 - j
                        if not walls[nx][ny-1]['R']:
                            temp[nx][ny-1] = 5 - j
                        if nx + 1 < r and not walls[nx+1][ny]['U'] and not walls[nx+1][ny-1]['R']:
                            temp[nx+1][ny-1] = 5 - j

        # UP
        elif direction == 3:
            temp[x-1][y] = 5
            for i in range(1, 5):
                if x - i - 1 < 0:
                    break
                nx = x - i
                for ny in range(y-i+1, y+i):
                    if 0 <= ny < c and temp[nx][ny] != -1:
                        if ny - 1 >= 0 and not walls[nx][ny-1]['U'] and not walls[nx][ny-1]['R']:
                            temp[nx-1][ny-1] = 5 - i
                        if not walls[nx][ny]['U']:
                            temp[nx-1][ny] = 5 - i
                        if ny + 1 < c and not walls[nx][ny+1]['U'] and not walls[nx][ny]['R']:
                            temp[nx-1][ny+1] = 5 - i

        # DOWN
        elif direction == 4:
            temp[x+1][y] = 5
            for i in range(1, 5):
                if x + i + 1 >= r:
                    break
                nx = x + i
                for ny in range(y-i+1, y+i):
                    if 0 <= ny < c and temp[nx][ny] != -1:
                        if ny - 1 >= 0 and not walls[nx+1][ny-1]['U'] and not walls[nx][ny-1]['R']:
                            temp[nx+1][ny-1] = 5 - i
                        if not walls[nx+1][ny]['U']:
                            temp[nx+1][ny] = 5 - i
                        if ny + 1 < c and not walls[nx+1][ny+1]['U'] and not walls[nx][ny]['R']:
                            temp[nx+1][ny+1] = 5 - i

        for i in range(r):
            for j in range(c):
                if temp[i][j] != -1:
                    result[i][j] += temp[i][j]

    return result


def reduce(t):
    temp = deepcopy(t)

    for i in range(r-1, -1, -1):
        for j in range(c):
            if i - 1 >= 0 and not walls[i][j]['U'] and t[i][j] != t[i-1][j]:
                if t[i][j] > t[i-1][j]:
                    diff = (t[i][j] - t[i-1][j]) // 4
                    temp[i][j] -= diff
                    temp[i-1][j] += diff
                elif t[i][j] < t[i-1][j]:
                    diff = (t[i-1][j] - t[i][j]) // 4
                    temp[i][j] += diff
                    temp[i-1][j] -= diff
            if j + 1 < c and not walls[i][j]['R'] and t[i][j] != t[i][j+1]:
                if t[i][j] > t[i][j+1]:
                    diff = (t[i][j] - t[i][j+1]) // 4
                    temp[i][j] -= diff
                    temp[i][j+1] += diff
                elif t[i][j] < t[i][j+1]:
                    diff = (t[i][j+1] - t[i][j]) // 4
                    temp[i][j] += diff
                    temp[i][j+1] -= diff

    return temp


while True:
    plused = wind()

    for i in range(r):
        for j in range(c):
            temperatures[i][j] += plused[i][j]

    temperatures = reduce(deepcopy(temperatures))

    for j in range(c):
        if temperatures[0][j] > 0:
            temperatures[0][j] -= 1
        if temperatures[r-1][j] > 0:
            temperatures[r-1][j] -= 1
    for i in range(1, r-1):
        if temperatures[i][0] > 0:
            temperatures[i][0] -= 1
        if temperatures[i][c-1] > 0:
            temperatures[i][c-1] -= 1

    choco += 1

    if choco > 100:
        print(101)
        break

    finish = True

    for x, y in targets:
        if temperatures[x][y] < k:
            finish = False
            break

    if finish:
        print(choco)
        break